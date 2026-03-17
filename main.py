import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
from tugas_ui import Ui_MainWindow


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image = None
        self.original_image = None  # simpan salinan gambar asli untuk reset
        self.result_image = None  # FIX #4: track last processed result

        # FILE
        self.ui.actionLoad_Image.triggered.connect(self.load_image)
        self.ui.actionSave_Image.triggered.connect(self.save_image)
        self.ui.actionReset_Image.triggered.connect(self.reset_image)

        # PRE PROCESSING
        self.ui.actionGrayscale_2.triggered.connect(self.grayscale)
        self.ui.actionBinary_2.triggered.connect(self.binary)

        # ENHANCEMENT
        self.ui.actionBrightness.triggered.connect(self.brightness)
        self.ui.actionContrast_Stretching.triggered.connect(self.contrast)
        self.ui.actionHistogram_Equalization.triggered.connect(self.histogram)

        # FILTERING
        self.ui.actionGaussian_Blur.triggered.connect(self.gaussian)
        self.ui.actionGaussian_Blur_2.triggered.connect(self.median)
        self.ui.actionSharpen.triggered.connect(self.sharpen)

        # EDGE
        self.ui.actionSobel.triggered.connect(self.sobel)
        self.ui.actionPrewitt.triggered.connect(self.prewitt)
        self.ui.actionCanny.triggered.connect(self.canny)

        # MORPHOLOGY
        self.ui.actionDilasi.triggered.connect(self.dilasi)
        self.ui.actionErosi.triggered.connect(self.erosi)
        self.ui.actionOpening.triggered.connect(self.opening)  # FIX #5: connect Opening
        self.ui.actionClosing.triggered.connect(self.closing)  # FIX #5: connect Closing

        # EKSTRA
        self.ui.actionExport_TXT.triggered.connect(self.export_txt)  # FIX #6
        self.ui.actionExport_Excel.triggered.connect(self.export_excel)  # FIX #6

    # ==========================
    # DISPLAY IMAGE
    # ==========================

    def display(self, img, label):

        if len(img.shape) == 2:
            qformat = QImage.Format_Grayscale8
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            qformat = QImage.Format_RGB888

        h, w = img.shape[:2]
        bytes_per_line = img.strides[0]

        qimg = QImage(img.data, w, h, bytes_per_line, qformat)

        label.setPixmap(QPixmap.fromImage(qimg))
        label.setScaledContents(True)

    # FIX #3: helper to guard all processing methods
    def check_image(self):
        if self.image is None:
            QMessageBox.warning(
                self, "Peringatan", "Silakan load gambar terlebih dahulu!"
            )
            return False
        return True

    # ==========================
    # FILE
    # ==========================

    def load_image(self):

        path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg)"
        )

        if path:
            self.image = cv2.imread(path)
            self.original_image = self.image.copy()  # simpan salinan asli
            self.result_image = None  # reset result on new load
            self.display(self.image, self.ui.label)
            self.ui.label_2.clear()

    def save_image(self):

        # FIX #4: save result image if available, otherwise save original
        img_to_save = self.result_image if self.result_image is not None else self.image

        if img_to_save is None:
            QMessageBox.warning(self, "Peringatan", "Tidak ada gambar untuk disimpan!")
            return

        path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG (*.png);;JPG (*.jpg)"
        )

        if path:
            cv2.imwrite(path, img_to_save)

    def reset_image(self):

        if self.original_image is None:
            QMessageBox.warning(self, "Peringatan", "Belum ada gambar yang di-load!")
            return

        self.image = self.original_image.copy()
        self.result_image = None
        self.display(self.image, self.ui.label)
        self.ui.label_2.clear()
        self.ui.statusbar.showMessage("Gambar berhasil direset ke kondisi awal.", 3000)

    # ==========================
    # PREPROCESS
    # ==========================

    def grayscale(self):

        if not self.check_image():  # FIX #3
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result_image = gray  # FIX #4
        self.display(gray, self.ui.label_2)

    def binary(self):

        if not self.check_image():  # FIX #3
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        self.result_image = binary  # FIX #4
        self.display(binary, self.ui.label_2)

    # ==========================
    # ENHANCEMENT
    # ==========================

    def brightness(self):

        if not self.check_image():  # FIX #3
            return

        bright = cv2.convertScaleAbs(self.image, beta=50)
        self.result_image = bright  # FIX #4
        self.display(bright, self.ui.label_2)

    def contrast(self):

        if not self.check_image():  # FIX #3
            return

        contrast = cv2.convertScaleAbs(self.image, alpha=1.8)
        self.result_image = contrast  # FIX #4
        self.display(contrast, self.ui.label_2)

    def histogram(self):

        if not self.check_image():  # FIX #3
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        hist_equalized = cv2.equalizeHist(gray)
        self.result_image = (
            hist_equalized  # FIX #4: save equalized image for export/save
        )

        def plot_histogram_panel(ax, img_data, title, bar_color, cdf_color):
            bin_centers = np.arange(256)
            hist, _ = np.histogram(img_data.ravel(), bins=256, range=[0, 256])

            # CDF in percent
            cdf = hist.cumsum()
            cdf_pct = cdf / cdf[-1] * 100

            mean_val = float(img_data.mean())

            # Background & grid
            ax.set_facecolor("#ebebeb")
            ax.grid(True, color="white", linewidth=0.8, zorder=0)

            # Histogram bars
            bar_handle = ax.bar(
                bin_centers,
                hist,
                color=bar_color,
                edgecolor="none",
                width=1.0,
                alpha=0.85,
                label="Histogram",
                zorder=2,
            )

            # Mean dashed line
            mean_line = ax.axvline(
                mean_val,
                color="red",
                linestyle="--",
                linewidth=1.5,
                label=f"Mean = {mean_val:.1f}",
                zorder=3,
            )

            ax.set_title(title, fontsize=10, fontweight="bold")
            ax.set_xlabel("Nilai Piksel", fontsize=9)
            ax.set_ylabel("Frekuensi", fontsize=9, color=bar_color)
            ax.tick_params(axis="y", labelcolor=bar_color)
            ax.set_xlim([0, 256])

            # Secondary y-axis for CDF
            ax2 = ax.twinx()
            (cdf_line,) = ax2.plot(
                bin_centers,
                cdf_pct,
                color=cdf_color,
                linewidth=2,
                label="CDF",
                zorder=4,
            )
            ax2.set_ylim([0, 100])
            ax2.set_ylabel("CDF", fontsize=9, color=cdf_color)
            ax2.tick_params(axis="y", labelcolor=cdf_color)
            ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}%"))

            # Combined legend on primary axis
            handles = [mean_line, bar_handle, cdf_line]
            ax.legend(handles=handles, loc="upper left", fontsize=8)

        fig_hist, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig_hist.patch.set_facecolor("#e0e0e0")
        fig_hist.suptitle("Histogram Equalization", fontsize=14, fontweight="bold")

        plot_histogram_panel(
            axes[0],
            gray,
            "Histogram Sebelum Equalization",
            bar_color="steelblue",
            cdf_color="orange",
        )
        plot_histogram_panel(
            axes[1],
            hist_equalized,
            "Histogram Sesudah Equalization",
            bar_color="#4caf8a",
            cdf_color="tomato",
        )

        # Tampilkan window baru untuk citra sebelum dan sesudah histogram equalization
        cv2.namedWindow("Citra Sebelum Equalization", cv2.WINDOW_NORMAL)
        cv2.imshow("Citra Sebelum Equalization", gray)
        cv2.namedWindow("Citra Sesudah Equalization", cv2.WINDOW_NORMAL)
        cv2.imshow("Citra Sesudah Equalization", hist_equalized)
        cv2.waitKey(1)

        plt.tight_layout()
        plt.show()

    # ==========================
    # FILTER
    # ==========================

    def gaussian(self):

        if not self.check_image():  # FIX #3
            return

        blur = cv2.GaussianBlur(self.image, (5, 5), 0)
        self.result_image = blur  # FIX #4
        self.display(blur, self.ui.label_2)

    def median(self):

        if not self.check_image():  # FIX #3
            return

        med = cv2.medianBlur(self.image, 5)
        self.result_image = med  # FIX #4
        self.display(med, self.ui.label_2)

    def sharpen(self):

        if not self.check_image():  # FIX #3
            return

        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

        sharp = cv2.filter2D(self.image, -1, kernel)
        self.result_image = sharp  # FIX #4
        self.display(sharp, self.ui.label_2)

    # ==========================
    # EDGE DETECTION
    # ==========================

    def sobel(self):

        if not self.check_image():  # FIX #3
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

        sobel = cv2.magnitude(sobelx, sobely)
        # FIX #1: convert float64 -> uint8 so QImage.Format_Grayscale8 displays correctly
        sobel = cv2.convertScaleAbs(sobel)

        self.result_image = sobel  # FIX #4
        self.display(sobel, self.ui.label_2)

    def prewitt(self):

        if not self.check_image():  # FIX #3
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

        # FIX #2: use CV_32F to avoid uint8 overflow, then compute magnitude and convert back
        x = cv2.filter2D(gray, cv2.CV_32F, kernelx)
        y = cv2.filter2D(gray, cv2.CV_32F, kernely)

        prewitt = cv2.magnitude(x, y)
        prewitt = cv2.convertScaleAbs(prewitt)

        self.result_image = prewitt  # FIX #4
        self.display(prewitt, self.ui.label_2)

    def canny(self):

        if not self.check_image():  # FIX #3
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        edge = cv2.Canny(gray, 100, 200)
        self.result_image = edge  # FIX #4
        self.display(edge, self.ui.label_2)

    # ==========================
    # MORPHOLOGY
    # ==========================

    def dilasi(self):

        if not self.check_image():  # FIX #3
            return

        kernel = np.ones((5, 5), np.uint8)
        dil = cv2.dilate(self.image, kernel, iterations=1)
        self.result_image = dil  # FIX #4
        self.display(dil, self.ui.label_2)

    def erosi(self):

        if not self.check_image():  # FIX #3
            return

        kernel = np.ones((5, 5), np.uint8)
        ero = cv2.erode(self.image, kernel, iterations=1)
        self.result_image = ero  # FIX #4
        self.display(ero, self.ui.label_2)

    # FIX #5: implement Opening (erosi lalu dilasi)
    def opening(self):

        if not self.check_image():  # FIX #3
            return

        kernel = np.ones((5, 5), np.uint8)
        opened = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)
        self.result_image = opened  # FIX #4
        self.display(opened, self.ui.label_2)

    # FIX #5: implement Closing (dilasi lalu erosi)
    def closing(self):

        if not self.check_image():  # FIX #3
            return

        kernel = np.ones((5, 5), np.uint8)
        closed = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
        self.result_image = closed  # FIX #4
        self.display(closed, self.ui.label_2)

    # ==========================
    # EKSTRA
    # ==========================

    # FIX #6: implement Export TXT
    def export_txt(self):

        img_to_export = (
            self.result_image if self.result_image is not None else self.image
        )

        if img_to_export is None:
            QMessageBox.warning(
                self, "Peringatan", "Silakan load gambar terlebih dahulu!"
            )
            return

        path, _ = QFileDialog.getSaveFileName(
            self, "Export TXT", "", "Text File (*.txt)"
        )

        if path:
            # Flatten to 2D for grayscale, or write channel-by-channel for color
            if len(img_to_export.shape) == 2:
                np.savetxt(path, img_to_export, fmt="%d")
            else:
                # Convert to grayscale before exporting as plain text matrix
                gray_export = cv2.cvtColor(img_to_export, cv2.COLOR_BGR2GRAY)
                np.savetxt(path, gray_export, fmt="%d")

            QMessageBox.information(self, "Sukses", "Gambar berhasil diekspor ke TXT!")

    # FIX #6: implement Export Excel
    def export_excel(self):

        try:
            import openpyxl
        except ImportError:
            QMessageBox.warning(
                self,
                "Error",
                "Library openpyxl belum terinstall.\nJalankan: pip install openpyxl",
            )
            return

        img_to_export = (
            self.result_image if self.result_image is not None else self.image
        )

        if img_to_export is None:
            QMessageBox.warning(
                self, "Peringatan", "Silakan load gambar terlebih dahulu!"
            )
            return

        path, _ = QFileDialog.getSaveFileName(
            self, "Export Excel", "", "Excel File (*.xlsx)"
        )

        if path:
            # Convert to grayscale for a clean single-sheet pixel matrix
            if len(img_to_export.shape) == 3:
                data = cv2.cvtColor(img_to_export, cv2.COLOR_BGR2GRAY)
            else:
                data = img_to_export

            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Pixel Values"

            for row in data.tolist():
                ws.append(row)

            wb.save(path)
            QMessageBox.information(
                self, "Sukses", "Gambar berhasil diekspor ke Excel!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainApp()
    window.show()

    sys.exit(app.exec_())

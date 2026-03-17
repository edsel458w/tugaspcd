import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from tugas_ui import Ui_MainWindow


class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image = None

        # FILE
        self.ui.actionLoad_Image.triggered.connect(self.load_image)
        self.ui.actionSave_Image.triggered.connect(self.save_image)

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

    # ==========================
    # FILE
    # ==========================

    def load_image(self):

        path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)")

        if path:
            self.image = cv2.imread(path)
            self.display(self.image, self.ui.label)

    def save_image(self):

        path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG (*.png);;JPG (*.jpg)")

        if path:
            cv2.imwrite(path, self.image)

    # ==========================
    # PREPROCESS
    # ==========================

    def grayscale(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.display(gray, self.ui.label_2)

    def binary(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        self.display(binary, self.ui.label_2)

    # ==========================
    # ENHANCEMENT
    # ==========================

    def brightness(self):

        bright = cv2.convertScaleAbs(self.image, beta=50)
        self.display(bright, self.ui.label_2)

    def contrast(self):

        contrast = cv2.convertScaleAbs(self.image, alpha=1.8)
        self.display(contrast, self.ui.label_2)

    def histogram(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        hist = cv2.equalizeHist(gray)

        self.display(hist, self.ui.label_2)

    # ==========================
    # FILTER
    # ==========================

    def gaussian(self):

        blur = cv2.GaussianBlur(self.image, (5,5), 0)
        self.display(blur, self.ui.label_2)

    def median(self):

        med = cv2.medianBlur(self.image, 5)
        self.display(med, self.ui.label_2)

    def sharpen(self):

        kernel = np.array([[0,-1,0],
                           [-1,5,-1],
                           [0,-1,0]])

        sharp = cv2.filter2D(self.image, -1, kernel)

        self.display(sharp, self.ui.label_2)

    # ==========================
    # EDGE DETECTION
    # ==========================

    def sobel(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1,0)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0,1)

        sobel = cv2.magnitude(sobelx, sobely)

        self.display(sobel, self.ui.label_2)

    def prewitt(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
        kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

        x = cv2.filter2D(gray,-1,kernelx)
        y = cv2.filter2D(gray,-1,kernely)

        prewitt = x + y

        self.display(prewitt, self.ui.label_2)

    def canny(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        edge = cv2.Canny(gray,100,200)

        self.display(edge, self.ui.label_2)

    # ==========================
    # MORPHOLOGY
    # ==========================

    def dilasi(self):

        kernel = np.ones((5,5),np.uint8)

        dil = cv2.dilate(self.image,kernel,iterations=1)

        self.display(dil, self.ui.label_2)

    def erosi(self):

        kernel = np.ones((5,5),np.uint8)

        ero = cv2.erode(self.image,kernel,iterations=1)

        self.display(ero, self.ui.label_2)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainApp()
    window.show()

    sys.exit(app.exec_())
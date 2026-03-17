# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 780)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ── Main vertical layout ──────────────────────────────────────────
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(10)

        # ── Row: two image panels side-by-side ────────────────────────────
        images_row = QtWidgets.QHBoxLayout()
        images_row.setSpacing(16)

        # Left panel ── Citra Awal
        left_col = QtWidgets.QVBoxLayout()
        left_col.setSpacing(6)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMinimumSize(QtCore.QSize(380, 280))
        self.label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding,
        )

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed,
        )
        font_caption = QtGui.QFont()
        font_caption.setPointSize(10)
        font_caption.setBold(True)
        self.label_3.setFont(font_caption)

        left_col.addWidget(self.label)
        left_col.addWidget(self.label_3)

        # Right panel ── Citra Hasil
        right_col = QtWidgets.QVBoxLayout()
        right_col.setSpacing(6)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setMinimumSize(QtCore.QSize(380, 280))
        self.label_2.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding,
        )

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed,
        )
        self.label_4.setFont(font_caption)

        right_col.addWidget(self.label_2)
        right_col.addWidget(self.label_4)

        images_row.addLayout(left_col)
        images_row.addLayout(right_col)

        main_layout.addLayout(images_row, stretch=3)

        MainWindow.setCentralWidget(self.centralwidget)

        # ── Menu bar ──────────────────────────────────────────────────────
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPre_processing = QtWidgets.QMenu(self.menubar)
        self.menuPre_processing.setObjectName("menuPre_processing")
        self.menuImage_Enhancement = QtWidgets.QMenu(self.menubar)
        self.menuImage_Enhancement.setObjectName("menuImage_Enhancement")
        self.menuFiltering = QtWidgets.QMenu(self.menubar)
        self.menuFiltering.setObjectName("menuFiltering")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuMorphology = QtWidgets.QMenu(self.menubar)
        self.menuMorphology.setObjectName("menuMorphology")
        self.menuEkstra = QtWidgets.QMenu(self.menubar)
        self.menuEkstra.setObjectName("menuEkstra")
        MainWindow.setMenuBar(self.menubar)

        # ── Status bar ────────────────────────────────────────────────────
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ── Actions ───────────────────────────────────────────────────────
        self.actionLoad_Image = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image.setObjectName("actionLoad_Image")

        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")

        self.actionReset_Image = QtWidgets.QAction(MainWindow)
        self.actionReset_Image.setObjectName("actionReset_Image")

        self.actionGrayscale = QtWidgets.QAction(MainWindow)
        self.actionGrayscale.setObjectName("actionGrayscale")

        self.actionBinary = QtWidgets.QAction(MainWindow)
        self.actionBinary.setObjectName("actionBinary")

        self.actionGrayscale_2 = QtWidgets.QAction(MainWindow)
        self.actionGrayscale_2.setObjectName("actionGrayscale_2")

        self.actionBinary_2 = QtWidgets.QAction(MainWindow)
        self.actionBinary_2.setObjectName("actionBinary_2")

        self.actionBrightness = QtWidgets.QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")

        self.actionContrast_Stretching = QtWidgets.QAction(MainWindow)
        self.actionContrast_Stretching.setObjectName("actionContrast_Stretching")

        self.actionHistogram_Equalization = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Equalization.setObjectName("actionHistogram_Equalization")

        self.actionGaussian_Blur = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur.setObjectName("actionGaussian_Blur")

        self.actionGaussian_Blur_2 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_2.setObjectName("actionGaussian_Blur_2")

        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")

        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")

        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")

        self.actionCanny = QtWidgets.QAction(MainWindow)
        self.actionCanny.setObjectName("actionCanny")

        self.actionDilasi = QtWidgets.QAction(MainWindow)
        self.actionDilasi.setObjectName("actionDilasi")

        self.actionErosi = QtWidgets.QAction(MainWindow)
        self.actionErosi.setObjectName("actionErosi")

        self.actionOpening = QtWidgets.QAction(MainWindow)
        self.actionOpening.setObjectName("actionOpening")

        self.actionClosing = QtWidgets.QAction(MainWindow)
        self.actionClosing.setObjectName("actionClosing")

        self.actionExport_TXT = QtWidgets.QAction(MainWindow)
        self.actionExport_TXT.setObjectName("actionExport_TXT")

        self.actionExport_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_Excel.setObjectName("actionExport_Excel")

        # ── Wire actions into menus ───────────────────────────────────────
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionReset_Image)

        self.menuPre_processing.addAction(self.actionGrayscale_2)
        self.menuPre_processing.addAction(self.actionBinary_2)

        self.menuImage_Enhancement.addAction(self.actionBrightness)
        self.menuImage_Enhancement.addAction(self.actionContrast_Stretching)
        self.menuImage_Enhancement.addAction(self.actionHistogram_Equalization)

        self.menuFiltering.addAction(self.actionGaussian_Blur)
        self.menuFiltering.addAction(self.actionGaussian_Blur_2)
        self.menuFiltering.addAction(self.actionSharpen)

        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menuEdge_Detection.addAction(self.actionCanny)

        self.menuMorphology.addAction(self.actionDilasi)
        self.menuMorphology.addAction(self.actionErosi)
        self.menuMorphology.addAction(self.actionOpening)
        self.menuMorphology.addAction(self.actionClosing)

        self.menuEkstra.addAction(self.actionExport_TXT)
        self.menuEkstra.addAction(self.actionExport_Excel)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPre_processing.menuAction())
        self.menubar.addAction(self.menuImage_Enhancement.menuAction())
        self.menubar.addAction(self.menuFiltering.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.menubar.addAction(self.menuMorphology.menuAction())
        self.menubar.addAction(self.menuEkstra.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing App"))
        self.label_3.setText(_translate("MainWindow", "Citra Awal"))
        self.label_4.setText(_translate("MainWindow", "Citra Hasil"))
       
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPre_processing.setTitle(_translate("MainWindow", "Pre-processing"))
        self.menuImage_Enhancement.setTitle(
            _translate("MainWindow", "Image Enhancement")
        )
        self.menuFiltering.setTitle(_translate("MainWindow", "Filtering"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuMorphology.setTitle(_translate("MainWindow", "Morphology"))
        self.menuEkstra.setTitle(_translate("MainWindow", "Ekstra"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionReset_Image.setText(_translate("MainWindow", "Reset Image"))
        self.actionGrayscale.setText(_translate("MainWindow", "Grayscale"))
        self.actionBinary.setText(_translate("MainWindow", "Binary"))
        self.actionGrayscale_2.setText(_translate("MainWindow", "Grayscale"))
        self.actionBinary_2.setText(_translate("MainWindow", "Binary"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionContrast_Stretching.setText(
            _translate("MainWindow", "Contrast Stretching")
        )
        self.actionHistogram_Equalization.setText(
            _translate("MainWindow", "Histogram Equalization")
        )
        self.actionGaussian_Blur.setText(_translate("MainWindow", "Gaussian Blur"))
        self.actionGaussian_Blur_2.setText(_translate("MainWindow", "Median Filter"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionCanny.setText(_translate("MainWindow", "Canny"))
        self.actionDilasi.setText(_translate("MainWindow", "Dilasi"))
        self.actionErosi.setText(_translate("MainWindow", "Erosi"))
        self.actionOpening.setText(_translate("MainWindow", "Opening"))
        self.actionClosing.setText(_translate("MainWindow", "Closing"))
        self.actionExport_TXT.setText(_translate("MainWindow", "Export TXT"))
        self.actionExport_Excel.setText(_translate("MainWindow", "Export Excel"))

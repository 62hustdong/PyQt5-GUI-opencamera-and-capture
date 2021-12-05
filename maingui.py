# Autho: Trinh Quang Dong
# Creat in: 2/12/2021

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUFJxav.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import time
import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os
import sys
import cv2


################################ function support #######################################
def convert_nparray_to_QPixmap(img):
    ## input: Anh mau RGB hoac anh xam
    ## output: Tao mot doi tuong QPixmax de hien thi bang cach chuyen du lieu anh sang mot doi tuong QImage
    ### print("{0} {1} {2}".format(img.shape[0], img.shape[1], img.ndim, ))
    if img.ndim == 2:
        w, h = img.shape
        # Convert resulting image to pixmap
        qimg = QImage(img.data, h, w, h, QImage.Format_Grayscale8)
        qpixmap = QPixmap(qimg)
        return qpixmap
    if img.ndim == 3:
        w, h, ch = img.shape
        # Convert resulting image to pixmap
        qimg = QImage(img.data, h, w, 3 * h, QImage.Format_RGB888).rgbSwapped()
        qpixmap = QPixmap(qimg)
        return qpixmap


def change_brightness(input_img, value):
    hsv = cv2.cvtColor(input_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    final_hsv = cv2.merge((h, s, v))
    output_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return output_img


def change_contrast(input_img, contrast=127):
    contrast = map(contrast, -50, 50, -127, 127)

    output_img = input_img.copy()
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        output_img = cv2.addWeighted(input_img, alpha_c, input_img, 0, gamma_c)
    return output_img


def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


################################ end function support ####################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 840)
        MainWindow.setFixedSize(1200, 840)
        self.actionImage = QAction(MainWindow)
        self.actionImage.setObjectName(u"actionImage")
        self.actionVideo = QAction(MainWindow)
        self.actionVideo.setObjectName(u"actionVideo")
        self.actionImage_2 = QAction(MainWindow)
        self.actionImage_2.setObjectName(u"actionImage_2")
        self.actionVideo_2 = QAction(MainWindow)
        self.actionVideo_2.setObjectName(u"actionVideo_2")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(510, 580, 471, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.prevBT = QPushButton(self.horizontalLayoutWidget_2)
        self.prevBT.setObjectName(u"prevBT")

        self.horizontalLayout_3.addWidget(self.prevBT)

        self.nextBT = QPushButton(self.horizontalLayoutWidget_2)
        self.nextBT.setObjectName(u"nextBT")

        self.horizontalLayout_3.addWidget(self.nextBT)

        self.exitBT = QPushButton(self.centralwidget)
        self.exitBT.setObjectName(u"exitBT")
        self.exitBT.setGeometry(QRect(980, 750, 93, 28))
        self.selectionGB = QGroupBox(self.centralwidget)
        self.selectionGB.setObjectName(u"selectionGB")
        self.selectionGB.setGeometry(QRect(340, 620, 841, 121))
        self.horizontalLayoutWidget_3 = QWidget(self.selectionGB)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(70, 70, 156, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cameraLB = QLabel(self.horizontalLayoutWidget_3)
        self.cameraLB.setObjectName(u"cameraLB")

        self.horizontalLayout_4.addWidget(self.cameraLB)

        self.openCameraBT = QPushButton(self.horizontalLayoutWidget_3)
        self.openCameraBT.setObjectName(u"openCameraBT")

        self.horizontalLayout_4.addWidget(self.openCameraBT)

        self.gridLayoutWidget_2 = QWidget(self.selectionGB)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(310, 70, 191, 31))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.segmentationLB = QLabel(self.gridLayoutWidget_2)
        self.segmentationLB.setObjectName(u"segmentationLB")

        self.gridLayout_2.addWidget(self.segmentationLB, 0, 0, 1, 1)

        self.segBT = QPushButton(self.gridLayoutWidget_2)
        self.segBT.setObjectName(u"segBT")

        self.gridLayout_2.addWidget(self.segBT, 0, 1, 1, 1)

        self.horizontalLayoutWidget_4 = QWidget(self.selectionGB)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(600, 70, 181, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.saveLB = QLabel(self.horizontalLayoutWidget_4)
        self.saveLB.setObjectName(u"saveLB")

        self.horizontalLayout_5.addWidget(self.saveLB)

        self.saveBT = QPushButton(self.horizontalLayoutWidget_4)
        self.saveBT.setObjectName(u"saveBT")

        self.horizontalLayout_5.addWidget(self.saveBT)

        self.imageGB = QGroupBox(self.centralwidget)
        self.imageGB.setObjectName(u"imageGB")
        self.imageGB.setGeometry(QRect(340, 10, 841, 551))
        self.imageGB.setSizeIncrement(QSize(0, 0))

        self.imageGB.setAutoFillBackground(False)
        self.imageGB.setStyleSheet(u"")
        self.imageGB.setFlat(False)
        self.imageGB.setCheckable(False)
        self.imageLabelLB = QLabel(self.imageGB)
        self.imageLabelLB.setObjectName(u"imageLabelLB")
        self.imageLabelLB.setGeometry(QRect(60, 20, 704, 520))
        self.imageLabelLB.setAutoFillBackground(False)
        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 750, 301, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.progressLB = QLabel(self.horizontalLayoutWidget_5)
        self.progressLB.setObjectName(u"progressLB")
        self.progressLB.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.progressLB)

        self.progressBar = QProgressBar(self.horizontalLayoutWidget_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setValue(24)

        self.horizontalLayout_6.addWidget(self.progressBar)

        self.fileGB = QGroupBox(self.centralwidget)
        self.fileGB.setObjectName(u"fileGB")
        self.fileGB.setGeometry(QRect(10, 10, 321, 731))
        self.horizontalLayoutWidget = QWidget(self.fileGB)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 680, 295, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.allBT = QPushButton(self.horizontalLayoutWidget)
        self.allBT.setObjectName(u"allBT")

        self.horizontalLayout_2.addWidget(self.allBT)

        self.deleteBT = QPushButton(self.horizontalLayoutWidget)
        self.deleteBT.setObjectName(u"deleteBT")

        self.horizontalLayout_2.addWidget(self.deleteBT)

        self.changeDirBT = QPushButton(self.horizontalLayoutWidget)
        self.changeDirBT.setObjectName(u"changeDirBT")

        self.horizontalLayout_2.addWidget(self.changeDirBT)

        self.imageTreeTV = QTreeView(self.fileGB)
        self.imageTreeTV.setObjectName(u"imageTreeTV")
        self.imageTreeTV.setGeometry(QRect(10, 50, 291, 611))
        self.imageTreeTV.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.imageTreeTV.setHeaderHidden(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 26))
        self.menuOpen = QMenu(self.menubar)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuSave = QMenu(self.menubar)
        self.menuSave.setObjectName(u"menuSave")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menuOpen.addAction(self.actionFile)
        self.menuOpen.addAction(self.actionImage)
        self.menuOpen.addAction(self.actionVideo)
        self.menuSave.addAction(self.actionImage_2)
        self.menuSave.addAction(self.actionVideo_2)
        self.menuExit.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main Gui", None))
        self.actionImage.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.actionVideo.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.actionImage_2.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.actionVideo_2.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.prevBT.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.nextBT.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.exitBT.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.selectionGB.setTitle(QCoreApplication.translate("MainWindow", u"L\u1ef1a ch\u1ecdn", None))
        self.cameraLB.setText(QCoreApplication.translate("MainWindow", u"Camera: ", None))
        self.openCameraBT.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.segmentationLB.setText(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.segBT.setText(QCoreApplication.translate("MainWindow", u"Seg", None))
        self.saveLB.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.saveBT.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.imageGB.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.progressLB.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.fileGB.setTitle(QCoreApplication.translate("MainWindow", u"Th\u01b0 m\u1ee5c", None))
        self.allBT.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.deleteBT.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.changeDirBT.setText(QCoreApplication.translate("MainWindow", u"Change dir", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
        # retranslateUi


class Ui_CameraWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cameraOptionGB = QGroupBox(self.centralwidget)
        self.cameraOptionGB.setObjectName(u"cameraOptionGB")
        self.cameraOptionGB.setGeometry(QRect(770, 10, 411, 261))
        self.verticalLayoutWidget_3 = QWidget(self.cameraOptionGB)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 50, 381, 191))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.chonCameraLB = QLabel(self.verticalLayoutWidget_3)
        self.chonCameraLB.setObjectName(u"chonCameraLB")

        self.gridLayout.addWidget(self.chonCameraLB, 0, 0, 1, 1)

        self.chonCamCB = QComboBox(self.verticalLayoutWidget_3)
        self.chonCamCB.setObjectName(u"chonCamCB")

        self.gridLayout.addWidget(self.chonCamCB, 0, 1, 1, 1)

        self.chonKenhLB = QLabel(self.verticalLayoutWidget_3)
        self.chonKenhLB.setObjectName(u"chonKenhLB")

        self.gridLayout.addWidget(self.chonKenhLB, 1, 0, 1, 1)

        self.chonKenhCB = QComboBox(self.verticalLayoutWidget_3)
        self.chonKenhCB.setObjectName(u"chonKenhCB")

        self.gridLayout.addWidget(self.chonKenhCB, 1, 1, 1, 1)

        self.horizontalLayout_8.addLayout(self.gridLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.smallScreenRB = QRadioButton(self.verticalLayoutWidget_3)
        self.smallScreenRB.setObjectName(u"smallScreenRB")
        self.smallScreenRB.setChecked(True)

        self.gridLayout_2.addWidget(self.smallScreenRB, 1, 0, 1, 1)

        self.orginalScreenRB = QRadioButton(self.verticalLayoutWidget_3)
        self.orginalScreenRB.setObjectName(u"orginalScreenRB")

        self.gridLayout_2.addWidget(self.orginalScreenRB, 2, 0, 1, 1)

        self.horizontalLayout_8.addLayout(self.gridLayout_2)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.doSangLB = QLabel(self.verticalLayoutWidget_3)
        self.doSangLB.setObjectName(u"doSangLB")
        self.doSangLB.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.doSangLB)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BrightnessSlider = QSlider(self.verticalLayoutWidget_3)
        self.BrightnessSlider.setObjectName(u"BrightnessSlider")
        self.BrightnessSlider.setMinimum(-50)
        self.BrightnessSlider.setMaximum(50)
        self.BrightnessSlider.setSliderPosition(0)
        self.BrightnessSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.BrightnessSlider)

        self.doubleSpinBox1 = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doubleSpinBox1.setObjectName(u"doubleSpinBox1")
        self.doubleSpinBox1.setDecimals(0)
        self.doubleSpinBox1.setMinimum(-50)
        self.doubleSpinBox1.setMaximum(50)
        self.doubleSpinBox1.setValue(0)

        self.horizontalLayout.addWidget(self.doubleSpinBox1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.doSangLB_2 = QLabel(self.verticalLayoutWidget_3)
        self.doSangLB_2.setObjectName(u"doSangLB_2")
        self.doSangLB_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.doSangLB_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ContrastSlider = QSlider(self.verticalLayoutWidget_3)
        self.ContrastSlider.setObjectName(u"ContrastSlider")
        self.ContrastSlider.setMinimum(-50)
        self.ContrastSlider.setMaximum(50)
        self.ContrastSlider.setSliderPosition(0)
        self.ContrastSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.ContrastSlider)

        self.doubleSpinBox2 = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doubleSpinBox2.setObjectName(u"doubleSpinBox2")
        self.doubleSpinBox2.setDecimals(0)
        self.doubleSpinBox2.setMinimum(-50)
        self.doubleSpinBox2.setMaximum(50)
        self.doubleSpinBox2.setValue(0)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.cameraGB = QGroupBox(self.centralwidget)
        self.cameraGB.setObjectName(u"cameraGB")
        self.cameraGB.setGeometry(QRect(20, 10, 741, 561))
        self.CameraLB = QLabel(self.cameraGB)
        self.CameraLB.setObjectName(u"CameraLB")
        self.CameraLB.setGeometry(QRect(20, 30, 704, 520))
        self.CameraLB.setAlignment(Qt.AlignCenter)
        self.captureOptionGB = QGroupBox(self.centralwidget)
        self.captureOptionGB.setObjectName(u"captureOptionGB")
        self.captureOptionGB.setGeometry(QRect(770, 280, 411, 291))
        self.verticalLayoutWidget_2 = QWidget(self.captureOptionGB)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 40, 391, 231))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.soLuongLB = QLabel(self.verticalLayoutWidget_2)
        self.soLuongLB.setObjectName(u"soLuongLB")

        self.horizontalLayout_2.addWidget(self.soLuongLB)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.x1RB = QRadioButton(self.verticalLayoutWidget_2)
        self.x1RB.setObjectName(u"x1RB")
        self.x1RB.setChecked(True)

        self.verticalLayout_2.addWidget(self.x1RB)

        self.x10RB = QRadioButton(self.verticalLayoutWidget_2)
        self.x10RB.setObjectName(u"x10RB")

        self.verticalLayout_2.addWidget(self.x10RB)

        self.x100RB = QRadioButton(self.verticalLayoutWidget_2)
        self.x100RB.setObjectName(u"x100RB")

        soLuongBG = QButtonGroup(self.verticalLayout_2)
        soLuongBG.addButton(self.x1RB)
        soLuongBG.addButton(self.x10RB)
        soLuongBG.addButton(self.x100RB)

        self.verticalLayout_2.addWidget(self.x100RB)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.kichThuocLB = QLabel(self.verticalLayoutWidget_2)
        self.kichThuocLB.setObjectName(u"kichThuocLB")

        self.horizontalLayout_3.addWidget(self.kichThuocLB)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.defaultRB = QRadioButton(self.verticalLayoutWidget_2)
        self.defaultRB.setObjectName(u"defaultRB")
        self.defaultRB.setChecked(True)

        self.verticalLayout_3.addWidget(self.defaultRB)

        self.i704x502RB = QRadioButton(self.verticalLayoutWidget_2)
        self.i704x502RB.setObjectName(u"i704x502RB")

        self.verticalLayout_3.addWidget(self.i704x502RB)

        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.i960x540RB = QRadioButton(self.verticalLayoutWidget_2)
        self.i960x540RB.setObjectName(u"i960x540RB")

        self.verticalLayout_5.addWidget(self.i960x540RB)

        self.i1280x960RB = QRadioButton(self.verticalLayoutWidget_2)
        self.i1280x960RB.setObjectName(u"i1280x960RB")

        kichThuocBG = QButtonGroup(self.horizontalLayout_7)
        kichThuocBG.addButton(self.defaultRB)
        kichThuocBG.addButton(self.i704x502RB)
        kichThuocBG.addButton(self.i960x540RB)
        kichThuocBG.addButton(self.i1280x960RB)

        self.verticalLayout_5.addWidget(self.i1280x960RB)

        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.waitTimeLB = QLabel(self.verticalLayoutWidget_2)
        self.waitTimeLB.setObjectName(u"waitTimeLB")
        self.waitTimeLB.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.waitTimeLB)

        self.doubleSpinBox3 = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox3.setObjectName(u"doubleSpinBox3")
        self.doubleSpinBox3.setDecimals(0)
        self.doubleSpinBox3.setMinimum(0)
        self.doubleSpinBox3.setMaximum(10000)
        self.doubleSpinBox3.setSingleStep(10)
        self.doubleSpinBox3.setValue(100)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox3)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.captureBT = QPushButton(self.verticalLayoutWidget_2)
        self.captureBT.setObjectName(u"captureBT")

        self.horizontalLayout_6.addWidget(self.captureBT)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.chonCamCB.addItem("Cam 0")
        self.chonCamCB.addItem("Cam 1")
        # self.chonCamCB.addItem("Cam 2")
        self.chonKenhCB.addItem("RGB")
        self.chonKenhCB.addItem("Gray")
        self.chonKenhCB.addItem("HSV")

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Camera Gui", None))
        self.cameraOptionGB.setTitle(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ecdn camera", None))
        self.chonCameraLB.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn camera:", None))
        self.chonKenhLB.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn k\u00eanh:", None))
        self.smallScreenRB.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh nh\u1ecf", None))
        self.orginalScreenRB.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh g\u1ed1c", None))
        self.doSangLB.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 s\u00e1ng", None))
        self.doSangLB_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 t\u01b0\u01a1ng ph\u1ea3n", None))
        self.cameraGB.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.CameraLB.setText("")
        self.captureOptionGB.setTitle(
            QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ch\u1ebf \u0111\u1ed9 ch\u1ee5p", None))
        self.soLuongLB.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        self.x1RB.setText(QCoreApplication.translate("MainWindow", u"1 \u1ea3nh", None))
        self.x10RB.setText(QCoreApplication.translate("MainWindow", u"10 \u1ea3nh", None))
        self.x100RB.setText(QCoreApplication.translate("MainWindow", u"100 \u1ea3nh", None))
        self.kichThuocLB.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc", None))
        self.defaultRB.setText(QCoreApplication.translate("MainWindow", u"M\u1eb7c \u0111\u1ecbnh", None))
        self.i704x502RB.setText(QCoreApplication.translate("MainWindow", u"704 x 520", None))
        self.i960x540RB.setText(QCoreApplication.translate("MainWindow", u"960 x 540", None))
        self.i1280x960RB.setText(QCoreApplication.translate("MainWindow", u"1280 x 960", None))
        self.waitTimeLB.setText(QCoreApplication.translate("MainWindow", u"Wait time [ms]", None))
        self.captureBT.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
    # retranslateUi


class CameraWindow(QMainWindow, Ui_CameraWindow):
    def __init__(self):
        super(CameraWindow, self).__init__()
        self.cap = None
        self.cam_curr_index = None
        self.kenh_curr_index = None
        self.frame = None
        self.frameGray = None
        self.frameHSV = None
        self.frameResize = None
        self.frameGrayResize = None
        self.frameHSVResize = None
        self.logic = 0
        self.chanel = 0
        self.cap_pix = None
        self.screen_show = 0
        self.brightness_adjuster = 0
        self.contrast_adjuster = 0
        self.waitTime = 100  # (ms)
        self.soLuong = 1
        self.kichThuoc = None
        self.writeImage = False
        self.timer = QTimer(self)
        self.myThread = None
        self.mydir = None
    def closeEvent(self, event):
        # close with X button
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            cv2.destroyAllWindows()
            self.cap.release()
            event.accept()
        else:
            event.ignore()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Camera Windown
        self.cameraWindow = CameraWindow()
        self.cameraWindow.setupUi(self.cameraWindow)

        # Load lai duong dan lan gan nhat
        f = open("K:\\PROJECT\\QT\\QT_APP_1\\APP\\test\\thamkhao\\save.txt", 'r')
        self.myRootPath = f.read()
        f.close()

        # Tao model de doc file trong system
        self.model = QFileSystemModel()
        self.model.setRootPath(self.myRootPath)

        # Cai dat imageTree (QTreeView)
        self.imageTreeTV.setModel(self.model)
        self.imageTreeTV.setRootIndex(self.model.index(self.myRootPath))
        self.imageTreeTV.setAnimated(False)
        self.imageTreeTV.setIndentation(20)
        self.imageTreeTV.setSortingEnabled(True)
        self.image_curr_index = self.imageTreeTV.rootIndex()  # de biet xem dang o anh nao

        # action
        ################### 1. action in mainwindow ##########################
        ################### 1.1 image tree action ######################

        self.imageTreeTV.clicked.connect(self.imageTreeTV_clicked)
        self.changeDirBT.clicked.connect(self.changeDirBT_clicked)
        self.deleteBT.clicked.connect(self.deleteBT_clicked)
        self.prevBT.clicked.connect(self.prevBT_clicked)
        self.nextBT.clicked.connect(self.nextBT_clicked)

        ################### 1.1 end image tree action ###################
        self.progressBar.hide()
        self.openCameraBT.clicked.connect(self.openCameraBT_clicked)
        self.cameraWindow.captureBT.clicked.connect(self.captureBT_clicked)
        self.segBT.clicked.connect(self.segBT_clicked)
        self.exitBT.clicked.connect(self.exitBT_clicked)
        self.actionFile.triggered.connect(self.actionFile_trigged)
        self.actionQuit.triggered.connect(self.actionQuit_trigged)
        ################# 1. end action in mainwindow ########################

        ################## 2. action in camerawindow #####################
        ################### 2.1 chonCameraCB action ######################
        self.camera_index = self.cameraWindow.chonCamCB.rootModelIndex()
        # de biet xem dang chon camera nao
        self.cameraWindow.chonCamCB.currentTextChanged.connect(self.chonCamCB_changed)
        ################### 2.1 end chonCameraCB action ####################

        ################### 2.2 chonKenhCB action ######################
        self.kenh_index = self.cameraWindow.chonCamCB.rootModelIndex()
        # de biet xem dang chon kenh nao
        self.cameraWindow.chonKenhCB.currentTextChanged.connect(self.chonKenhCB_changed)
        ################### 2.2 chonKenhCB action ######################

        ################### 2.3 chon screen action ######################
        self.cameraWindow.smallScreenRB.toggled.connect(self.smallScreenRB_toggled)
        self.cameraWindow.orginalScreenRB.toggled.connect(self.fullScreenRB_toggled)
        ################### 2.3 chon screen action ######################

        ################### 2.4 thay doi do sang action ##################
        self.cameraWindow.BrightnessSlider.valueChanged[int].connect(self.BrightnessSlider_valueChanged)
        self.cameraWindow.doubleSpinBox1.valueChanged.connect(self.doubleSpinBox1_valueChanged)
        ################### 2.4 end thay doi do sang action ##############

        ################### 2.5 thay doi do tuong phan action #############
        self.cameraWindow.ContrastSlider.valueChanged[int].connect(self.ContrastSlider_valueChanged)
        self.cameraWindow.doubleSpinBox2.valueChanged.connect(self.doubleSpinBox2_valueChanged)
        ################### 2.5 end thay doi do tuong phan action ##########

        ################### 2.6 thay doi thoi gian cho action #############
        self.cameraWindow.doubleSpinBox3.valueChanged.connect(self.doubleSpinBox3_valueChanged)
        ################### 2.6 end thay doi thoi gian cho action ##########

        ################### 2.7 thay doi so luong anh action #############
        self.cameraWindow.x1RB.toggled.connect(self.x1RB_toggled)
        self.cameraWindow.x10RB.toggled.connect(self.x10RB_toggled)
        self.cameraWindow.x100RB.toggled.connect(self.x100RB_toggled)

        ################### 2.7 end thay doi so luong anh action ##########

        ################### 2.8 thay doi kich thuoc anh action #############
        self.cameraWindow.defaultRB.toggled.connect(self.defaultRB_toggled)
        self.cameraWindow.i704x502RB.toggled.connect(self.i704x502RB_toggled)
        self.cameraWindow.i960x540RB.toggled.connect(self.i960x540RB_toggled)
        self.cameraWindow.i1280x960RB.toggled.connect(self.i1280x960RB_toggled)
        ################### 2.8 end thay doi kich thuoc anh action ##########

    ################## 2. end action in camerawindow #################

    ################### functions ###################

    def cameraRun(self):
        self.cameraWindow.cap = cv2.VideoCapture(self.cameraWindow.logic, cv2.CAP_DSHOW)
        # self.cameraWindow.cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
        # Using cv2.CAP_DSHOW removes the warning, but slows down my frame rate from 30fps to 7fps, on Windows
        if not self.cameraWindow.cap.isOpened():
            QMessageBox.warning(self.cameraWindow, "Warning", "Camera is not connected")
        while self.cameraWindow.cap.isOpened():
            # Capture the video frame
            # by frame
            ret, self.cameraWindow.frame = self.cameraWindow.cap.read()
            if self.cameraWindow.screen_show == 0:
                cv2.destroyAllWindows()
                if self.cameraWindow.frame.shape[0] / 520 > 1 or self.cameraWindow.frame.shape[1] / 704 > 1:
                    if self.cameraWindow.frame.shape[0] / 520 >= self.cameraWindow.frame.shape[1] / 704:
                        scale_ratio = 520 / self.cameraWindow.frame.shape[0]
                        width = int(self.cameraWindow.frame.shape[1] * scale_ratio)
                        height = 520
                        dim = (width, height)
                        self.cameraWindow.frameResize = cv2.resize(self.cameraWindow.frame, dim)
                    else:
                        scale_ratio = 704 / self.cameraWindow.frame.shape[1]
                        height = int(self.cameraWindow.frame.shape[0] * scale_ratio)
                        width = 704
                        dim = (width, height)
                        self.cameraWindow.frameResize = cv2.resize(self.cameraWindow.frame, dim)
                else:
                    self.cameraWindow.frameResize = self.cameraWindow.frame
                    # Display the resulting frame
                if self.cameraWindow.chanel == 0:
                    self.cameraWindow.frameResize = change_brightness(self.cameraWindow.frameResize,
                                                                      self.cameraWindow.brightness_adjuster)
                    self.cameraWindow.frameResize = change_contrast(self.cameraWindow.frameResize,
                                                                    self.cameraWindow.contrast_adjuster)
                    self.cameraWindow.cap_pix = convert_nparray_to_QPixmap(self.cameraWindow.frameResize)

                if self.cameraWindow.chanel == 1:
                    self.cameraWindow.frameGrayResize = cv2.cvtColor(self.cameraWindow.frameResize, cv2.COLOR_BGR2GRAY)
                    self.cameraWindow.cap_pix = convert_nparray_to_QPixmap(self.cameraWindow.frameGrayResize)

                if self.cameraWindow.chanel == 2:
                    self.cameraWindow.frameHSVResize = cv2.cvtColor(self.cameraWindow.frameResize, cv2.COLOR_BGR2HSV)
                    self.cameraWindow.cap_pix = convert_nparray_to_QPixmap(self.cameraWindow.frameHSVResize)
                self.cameraWindow.CameraLB.setPixmap(self.cameraWindow.cap_pix)
            else:
                if self.cameraWindow.chanel == 0:
                    self.cameraWindow.frame = change_brightness(self.cameraWindow.frame,
                                                                self.cameraWindow.brightness_adjuster)
                    self.cameraWindow.frame = change_contrast(self.cameraWindow.frame,
                                                              self.cameraWindow.contrast_adjuster)
                    cv2.imshow("RGB image", self.cameraWindow.frame)

                if self.cameraWindow.chanel == 1:
                    self.cameraWindow.frameGray = cv2.cvtColor(self.cameraWindow.frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Gray image", self.cameraWindow.frameGray)

                if self.cameraWindow.chanel == 2:
                    self.cameraWindow.frameHSV = cv2.cvtColor(self.cameraWindow.frame, cv2.COLOR_BGR2HSV)
                    cv2.imshow("HSV image", self.cameraWindow.frameHSV)
                # if self.cameraWindow.waitTime:
                #     self.saveImage()
                #     print(self.cameraWindow.waitTime)
                # self.cameraWindow.waitTime = False
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def chonCamCB_changed(self):
        chonCamText = self.cameraWindow.chonCamCB.currentText()
        if chonCamText == "Cam 1":
            self.cameraWindow.cam_curr_index = self.cameraWindow.chonCamCB.currentIndex()
            self.cameraWindow.logic = 1
            self.cameraRun()
        if chonCamText == "Cam 0":
            self.cameraWindow.cam_curr_index = self.cameraWindow.chonCamCB.currentIndex()
            self.cameraWindow.logic = 0
            self.cameraRun()

    def chonKenhCB_changed(self):
        chonKenhText = self.cameraWindow.chonKenhCB.currentText()
        if chonKenhText == "RGB":
            self.cameraWindow.chanel = 0
            cv2.destroyAllWindows()
        if chonKenhText == "Gray":
            self.cameraWindow.chanel = 1
            cv2.destroyAllWindows()
        if chonKenhText == "HSV":
            self.cameraWindow.chanel = 2
            cv2.destroyAllWindows()
        # print(chonKenhText)

    def smallScreenRB_toggled(self):
        self.cameraWindow.screen_show = 0

    def fullScreenRB_toggled(self):
        self.cameraWindow.screen_show = 1

    def BrightnessSlider_valueChanged(self, value):
        self.cameraWindow.brightness_adjuster = value
        self.cameraWindow.doubleSpinBox1.setValue(value)

    def doubleSpinBox1_valueChanged(self, value):
        self.cameraWindow.brightness_adjuster = value
        self.cameraWindow.BrightnessSlider.setValue(value)

    def ContrastSlider_valueChanged(self, value):
        self.cameraWindow.contrast_adjuster = value
        self.cameraWindow.doubleSpinBox2.setValue(value)

    def doubleSpinBox2_valueChanged(self, value):
        self.cameraWindow.contrast_adjuster = value
        self.cameraWindow.ContrastSlider.setValue(value)

    def doubleSpinBox3_valueChanged(self, value):
        self.cameraWindow.waitTime = value

    def x1RB_toggled(self):
        self.cameraWindow.soLuong = 1

    def x10RB_toggled(self):
        self.cameraWindow.soLuong = 10

    def x100RB_toggled(self):
        self.cameraWindow.soLuong = 100

    def defaultRB_toggled(self):
        self.cameraWindow.kichThuoc = (self.cameraWindow.frame.shape[0], self.cameraWindow.frame.shape[1])

    def i704x502RB_toggled(self):
        self.cameraWindow.kichThuoc = (502, 704)

    def i960x540RB_toggled(self):
        self.cameraWindow.kichThuoc = (540, 960)

    def i1280x960RB_toggled(self):
        self.cameraWindow.kichThuoc = (960, 1180)
        ################### image tree function ###################

    def imageTreeTV_clicked(self):
        self.image_curr_index = self.imageTreeTV.currentIndex()
        filePath = self.model.filePath(self.image_curr_index)
        # os.startfile(filePath)
        # print(filePath)
        if not self.model.isDir(self.image_curr_index):
            if self.model.type(self.image_curr_index) == 'jpg File' or self.model.type(
                    self.image_curr_index) == 'png File':
                img = cv2.imread(filePath, cv2.IMREAD_COLOR)
                img_resize = cv2.resize(img, (704, 520), 0, 0)
                pixmap = convert_nparray_to_QPixmap(img_resize)
                self.imageLabelLB.setPixmap(pixmap)

    def changeDirBT_clicked(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select a folder")
        self.myRootPath = folder_name
        self.model.setRootPath(self.myRootPath)
        self.imageTreeTV.setModel(self.model)
        self.imageTreeTV.setRootIndex(self.model.index(self.myRootPath))
        print('My foder:  {}'.format(folder_name))

    def deleteBT_clicked(self):
        index = self.imageTreeTV.currentIndex()
        filePath = self.model.filePath(index)
        mes = QMessageBox()
        reply = mes.warning(self, 'Wanning',
                            "Do you want delete file " + filePath + "?", QMessageBox.Yes |
                            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.remove(filePath)
        else:
            mes.close()

    def prevBT_clicked(self):
        prev_index = self.imageTreeTV.indexAbove(self.image_curr_index)

        self.image_curr_index = prev_index

        filePath = self.model.filePath(self.image_curr_index)
        if not self.model.isDir(self.image_curr_index):
            if self.model.type(self.image_curr_index) == 'jpg File' or self.model.type(
                    self.image_curr_index) == 'png File':
                img = cv2.imread(filePath, cv2.IMREAD_COLOR)
                img_resize = cv2.resize(img, (704, 520), 0, 0)
                pixmap = convert_nparray_to_QPixmap(img_resize)
                self.imageLabelLB.setPixmap(pixmap)

    def nextBT_clicked(self):
        next_index = self.imageTreeTV.indexBelow(self.image_curr_index)

        self.image_curr_index = next_index

        filePath = self.model.filePath(self.image_curr_index)
        if not self.model.isDir(self.image_curr_index):
            if self.model.type(self.image_curr_index) == 'jpg File' or self.model.type(
                    self.image_curr_index) == 'png File':
                img = cv2.imread(filePath, cv2.IMREAD_COLOR)
                img_resize = cv2.resize(img, (704, 520), 0, 0)
                pixmap = convert_nparray_to_QPixmap(img_resize)
                self.imageLabelLB.setPixmap(pixmap)

    ################### end image tree function ###################

    ################### actionFile function ######################

    def actionFile_trigged(self):
        self.changeDirBT_clicked()

    ################### end actionFile function ##################

    ################### option function ##########################

    ################### end option function ######################
    def openCameraBT_clicked(self):
        # when click openCamera button , show opencamera_ui
        if self.cameraWindow.isVisible():
            self.cameraWindow.hide()
        else:
            self.cameraWindow.show()
            self.cameraRun()

    def captureBT_clicked(self):

        self.cameraWindow.mydir = self.myRootPath + '/' + time.strftime("%d-%m-%Y-%H-%M-%S")
        os.mkdir(self.cameraWindow.mydir)
        self.cameraWindow.myThread = threading.Thread(target=self.saveImage,
                                                      args=(self.cameraWindow.soLuong,))
        self.cameraWindow.myThread.start()

    def saveImage(self, _soLuong):
        _soLuong = self.cameraWindow.soLuong
        _waitTime = self.cameraWindow.waitTime
        index = 0
        while _soLuong != 0:
            print(_soLuong)
            time.sleep(_waitTime * 0.001)
            cv2.imwrite("{}/{}".format(self.cameraWindow.mydir,index) + ".png", self.cameraWindow.frame)
            _soLuong = _soLuong - 1
            index = index + 1

        # cv2.imwrite('K:\\PROJECT\\QT\\QT_APP_1\\APP\\test\\test_thread\\test_save\\' + "frame-" + time.strftime(
        #     "%d-%m-%Y-%H-%M-%S") + ".png", self.cameraWindow.frame)
        # cv2.imwrite('K:\\PROJECT\\QT\\QT_APP_1\\APP\\test\\test_thread\\test_save\\' +
        # "frame-{}".format(time.strftime("%d-%m-%Y-%H-%M-%S")) + "{}".format(index) + ".png", self.cameraWindow.frame)
    def segBT_clicked(self):
        image = QImage("K://PROJECT//QT//QT_APP_1//APP//Project//picture//anh_sgm.png")
        display_image = QPixmap.fromImage(image)
        self.imageLabelLB.setPixmap(display_image)

        ################ close app ########################

    def exitBT_clicked(self):
        # when click exitBT button , close all screen
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            f = open("K:\\PROJECT\\QT\\QT_APP_1\\APP\\test\\thamkhao\\save.txt", "w")
            f.write(self.myRootPath)
            f.close()
            QCoreApplication.instance().quit()

    def closeEvent(self, event):
        # close with X button
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            f = open("K:\\PROJECT\\QT\\QT_APP_1\\APP\\test\\thamkhao\\save.txt", "w")
            f.write(self.myRootPath)
            f.close()
            event.accept()

        else:
            event.ignore()

    def actionQuit_trigged(self):
        self.exitBT_click(self)
        ####################################################


############################# end functions #########################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle('Windows')
    # setStyle ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    ui = MainWindow()
    ui.show()

    sys.exit(app.exec_())

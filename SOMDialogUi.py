# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SOMdialogBox.ui',
# licensing of 'SOMdialogBox.ui' applies.
#
# Created: Tue May 21 15:55:59 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SomInit(object):
    def setupUi(self, SomInit):
        SomInit.setObjectName("SomInit")
        SomInit.resize(323, 139)
        self.buttonBox = QtWidgets.QDialogButtonBox(SomInit)
        self.buttonBox.setGeometry(QtCore.QRect(240, 40, 77, 58))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(SomInit)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 236, 112))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.heightSB = QtWidgets.QSpinBox(self.layoutWidget)
        self.heightSB.setMinimum(10)
        self.heightSB.setMaximum(250)
        self.heightSB.setProperty("value", 25)
        self.heightSB.setObjectName("heightSB")
        self.gridLayout.addWidget(self.heightSB, 1, 0, 1, 1)
        self.widthSB = QtWidgets.QSpinBox(self.layoutWidget)
        self.widthSB.setMinimum(10)
        self.widthSB.setMaximum(250)
        self.widthSB.setProperty("value", 25)
        self.widthSB.setObjectName("widthSB")
        self.gridLayout.addWidget(self.widthSB, 0, 0, 1, 1)

        self.retranslateUi(SomInit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SomInit.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SomInit.reject)
        QtCore.QMetaObject.connectSlotsByName(SomInit)

    def retranslateUi(self, SomInit):
        SomInit.setWindowTitle(QtWidgets.QApplication.translate("SomInit", "Init SOM", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SomInit", "Height", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SomInit", "Width", None, -1))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SOMdialogBox.ui'
#
# Created: Wed May 10 14:02:49 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SomInit(object):
    def setupUi(self, SomInit):
        SomInit.setObjectName("SomInit")
        SomInit.resize(376, 139)
        self.buttonBox = QtGui.QDialogButtonBox(SomInit)
        self.buttonBox.setGeometry(QtCore.QRect(240, 10, 77, 58))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtGui.QWidget(SomInit)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 236, 112))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.heightSB = QtGui.QSpinBox(self.layoutWidget)
        self.heightSB.setMinimum(10)
        self.heightSB.setMaximum(250)
        self.heightSB.setProperty("value", 25)
        self.heightSB.setObjectName("heightSB")
        self.gridLayout.addWidget(self.heightSB, 1, 0, 1, 1)
        self.widthSB = QtGui.QSpinBox(self.layoutWidget)
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
        SomInit.setWindowTitle(QtGui.QApplication.translate("SomInit", "Init SOM", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SomInit", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SomInit", "Width", None, QtGui.QApplication.UnicodeUTF8))


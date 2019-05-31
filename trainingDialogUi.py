# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainingDialog.ui',
# licensing of 'trainingDialog.ui' applies.
#
# Created: Tue May 21 15:56:28 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TrainingDialog(object):
    def setupUi(self, TrainingDialog):
        TrainingDialog.setObjectName("TrainingDialog")
        TrainingDialog.resize(300, 175)
        self.gridLayout = QtWidgets.QGridLayout(TrainingDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.trainPropBox = QtWidgets.QWidget(TrainingDialog)
        self.trainPropBox.setObjectName("trainPropBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.trainPropBox)
        self.label = QtWidgets.QLabel(TrainingDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label)
        self.label_2 = QtWidgets.QLabel(TrainingDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.trainSpinBox = QtWidgets.QSpinBox(TrainingDialog)
        self.trainSpinBox.setObjectName("trainSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.trainSpinBox)
        self.trainSpeedSpinBox = QtWidgets.QDoubleSpinBox(TrainingDialog)
        self.trainSpeedSpinBox.setObjectName("trainSpeedSpinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.trainSpeedSpinBox)
        self.label_3 = QtWidgets.QLabel(TrainingDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.trainNeigborhood = QtWidgets.QSpinBox(TrainingDialog)
        self.trainNeigborhood.setObjectName("trainNeigborhood")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.trainNeigborhood)
        self.buttonBox = QtWidgets.QDialogButtonBox(TrainingDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.buttonBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(TrainingDialog)
        QtCore.QMetaObject.connectSlotsByName(TrainingDialog)

    def retranslateUi(self, TrainingDialog):
        TrainingDialog.setWindowTitle(QtWidgets.QApplication.translate("TrainingDialog", "TrainingDialog", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("TrainingDialog", "Iterations", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("TrainingDialog", "Trainig speed", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("TrainingDialog", "Neigborhood size", None, -1))


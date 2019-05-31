# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainingDataWindow.ui',
# licensing of 'trainingDataWindow.ui' applies.
#
# Created: Tue May 21 15:55:08 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_trainingDataWin(object):
    def setupUi(self, trainingDataWin):
        trainingDataWin.setObjectName("trainingDataWin")
        trainingDataWin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(trainingDataWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.trainingData = QtWidgets.QTableWidget(self.centralwidget)
        self.trainingData.setObjectName("trainingData")
        self.trainingData.setColumnCount(0)
        self.trainingData.setRowCount(0)
        self.gridLayout.addWidget(self.trainingData, 0, 0, 1, 1)
        trainingDataWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(trainingDataWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuLoad = QtWidgets.QMenu(self.menubar)
        self.menuLoad.setObjectName("menuLoad")
        trainingDataWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(trainingDataWin)
        self.statusbar.setObjectName("statusbar")
        trainingDataWin.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(trainingDataWin)
        self.actionLoad.setObjectName("actionLoad")
        self.actionQuit = QtWidgets.QAction(trainingDataWin)
        self.actionQuit.setObjectName("actionQuit")
        self.menuLoad.addAction(self.actionLoad)
        self.menuLoad.addAction(self.actionQuit)
        self.menubar.addAction(self.menuLoad.menuAction())

        self.retranslateUi(trainingDataWin)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), trainingDataWin.close)
        QtCore.QMetaObject.connectSlotsByName(trainingDataWin)

    def retranslateUi(self, trainingDataWin):
        trainingDataWin.setWindowTitle(QtWidgets.QApplication.translate("trainingDataWin", "Training data", None, -1))
        self.menuLoad.setTitle(QtWidgets.QApplication.translate("trainingDataWin", "File", None, -1))
        self.actionLoad.setText(QtWidgets.QApplication.translate("trainingDataWin", "Load data", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("trainingDataWin", "Close", None, -1))


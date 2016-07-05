# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainingDataWindow.ui'
#
# Created: Fri Jun 24 12:31:42 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_trainingDataWin(object):
    def setupUi(self, trainingDataWin):
        trainingDataWin.setObjectName("trainingDataWin")
        trainingDataWin.resize(800, 600)
        self.centralwidget = QtGui.QWidget(trainingDataWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.trainingData = QtGui.QTableWidget(self.centralwidget)
        self.trainingData.setObjectName("trainingData")
        self.trainingData.setColumnCount(0)
        self.trainingData.setRowCount(0)
        self.gridLayout.addWidget(self.trainingData, 0, 0, 1, 1)
        trainingDataWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(trainingDataWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuLoad = QtGui.QMenu(self.menubar)
        self.menuLoad.setObjectName("menuLoad")
        trainingDataWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(trainingDataWin)
        self.statusbar.setObjectName("statusbar")
        trainingDataWin.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(trainingDataWin)
        self.actionLoad.setObjectName("actionLoad")
        self.actionQuit = QtGui.QAction(trainingDataWin)
        self.actionQuit.setObjectName("actionQuit")
        self.menuLoad.addAction(self.actionLoad)
        self.menuLoad.addAction(self.actionQuit)
        self.menubar.addAction(self.menuLoad.menuAction())

        self.retranslateUi(trainingDataWin)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), trainingDataWin.close)
        QtCore.QMetaObject.connectSlotsByName(trainingDataWin)

    def retranslateUi(self, trainingDataWin):
        trainingDataWin.setWindowTitle(QtGui.QApplication.translate("trainingDataWin", "Trainind data", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLoad.setTitle(QtGui.QApplication.translate("trainingDataWin", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("trainingDataWin", "Load data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("trainingDataWin", "Close", None, QtGui.QApplication.UnicodeUTF8))


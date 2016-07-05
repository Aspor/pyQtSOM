# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_trainingDataLoader.ui'
#
# Created: Fri Jun 24 12:30:53 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TrainingDataLoader(object):
    def setupUi(self, TrainingDataLoader):
        TrainingDataLoader.setObjectName("TrainingDataLoader")
        TrainingDataLoader.resize(800, 600)
        self.centralwidget = QtGui.QWidget(TrainingDataLoader)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Data = QtGui.QTableWidget(self.centralwidget)
        self.Data.setObjectName("Data")
        self.Data.setColumnCount(0)
        self.Data.setRowCount(0)
        self.gridLayout.addWidget(self.Data, 0, 0, 1, 1)
        TrainingDataLoader.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TrainingDataLoader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TrainingDataLoader.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TrainingDataLoader)
        self.statusbar.setObjectName("statusbar")
        TrainingDataLoader.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(TrainingDataLoader)
        self.toolBar.setObjectName("toolBar")
        TrainingDataLoader.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(TrainingDataLoader)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtGui.QAction(TrainingDataLoader)
        self.actionClose.setObjectName("actionClose")
        self.actionLoad = QtGui.QAction(TrainingDataLoader)
        self.actionLoad.setObjectName("actionLoad")
        self.actionTranspose = QtGui.QAction(TrainingDataLoader)
        self.actionTranspose.setCheckable(True)
        self.actionTranspose.setObjectName("actionTranspose")
        self.actionSelectAll = QtGui.QAction(TrainingDataLoader)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionHeaders = QtGui.QAction(TrainingDataLoader)
        self.actionHeaders.setCheckable(True)
        self.actionHeaders.setObjectName("actionHeaders")
        self.actionLabels = QtGui.QAction(TrainingDataLoader)
        self.actionLabels.setCheckable(True)
        self.actionLabels.setObjectName("actionLabels")
        self.actionInitNetwork = QtGui.QAction(TrainingDataLoader)
        self.actionInitNetwork.setCheckable(True)
        self.actionInitNetwork.setChecked(True)
        self.actionInitNetwork.setObjectName("actionInitNetwork")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionHeaders)
        self.toolBar.addAction(self.actionLabels)
        self.toolBar.addAction(self.actionTranspose)
        self.toolBar.addAction(self.actionInitNetwork)

        self.retranslateUi(TrainingDataLoader)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL("triggered()"), TrainingDataLoader.close)
        QtCore.QObject.connect(self.actionSelectAll, QtCore.SIGNAL("triggered()"), self.Data.selectAll)
        QtCore.QMetaObject.connectSlotsByName(TrainingDataLoader)

    def retranslateUi(self, TrainingDataLoader):
        TrainingDataLoader.setWindowTitle(QtGui.QApplication.translate("TrainingDataLoader", "Load training data", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("TrainingDataLoader", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("TrainingDataLoader", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("TrainingDataLoader", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("TrainingDataLoader", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("TrainingDataLoader", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTranspose.setText(QtGui.QApplication.translate("TrainingDataLoader", "Transpose", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setText(QtGui.QApplication.translate("TrainingDataLoader", "SelectAll", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHeaders.setText(QtGui.QApplication.translate("TrainingDataLoader", "Headers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLabels.setText(QtGui.QApplication.translate("TrainingDataLoader", "Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInitNetwork.setText(QtGui.QApplication.translate("TrainingDataLoader", "Init network", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_trainingDataLoader.ui',
# licensing of 'ui_trainingDataLoader.ui' applies.
#
# Created: Tue May 21 15:59:26 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TrainingDataLoader(object):
    def setupUi(self, TrainingDataLoader):
        TrainingDataLoader.setObjectName("TrainingDataLoader")
        TrainingDataLoader.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TrainingDataLoader)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Data = QtWidgets.QTableWidget(self.centralwidget)
        self.Data.setObjectName("Data")
        self.Data.setColumnCount(0)
        self.Data.setRowCount(0)
        self.gridLayout.addWidget(self.Data, 0, 0, 1, 1)
        TrainingDataLoader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TrainingDataLoader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TrainingDataLoader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TrainingDataLoader)
        self.statusbar.setObjectName("statusbar")
        TrainingDataLoader.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(TrainingDataLoader)
        self.toolBar.setObjectName("toolBar")
        TrainingDataLoader.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(TrainingDataLoader)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(TrainingDataLoader)
        self.actionClose.setObjectName("actionClose")
        self.actionLoad = QtWidgets.QAction(TrainingDataLoader)
        self.actionLoad.setObjectName("actionLoad")
        self.actionTranspose = QtWidgets.QAction(TrainingDataLoader)
        self.actionTranspose.setCheckable(True)
        self.actionTranspose.setObjectName("actionTranspose")
        self.actionSelectAll = QtWidgets.QAction(TrainingDataLoader)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionHeaders = QtWidgets.QAction(TrainingDataLoader)
        self.actionHeaders.setCheckable(True)
        self.actionHeaders.setObjectName("actionHeaders")
        self.actionLabels = QtWidgets.QAction(TrainingDataLoader)
        self.actionLabels.setCheckable(True)
        self.actionLabels.setObjectName("actionLabels")
        self.actionInitNetwork = QtWidgets.QAction(TrainingDataLoader)
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
        TrainingDataLoader.setWindowTitle(QtWidgets.QApplication.translate("TrainingDataLoader", "Load training data", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("TrainingDataLoader", "File", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("TrainingDataLoader", "toolBar", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "Open", None, -1))
        self.actionClose.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "Close", None, -1))
        self.actionLoad.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "Load", None, -1))
        self.actionTranspose.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "Transpose", None, -1))
        self.actionSelectAll.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "SelectAll", None, -1))
        self.actionHeaders.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "Headers", None, -1))
        self.actionLabels.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "Labels", None, -1))
        self.actionInitNetwork.setText(QtWidgets.QApplication.translate("TrainingDataLoader", "Init network", None, -1))


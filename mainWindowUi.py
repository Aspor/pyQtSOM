# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui',
# licensing of 'ui_mainwindow.ui' applies.
#
# Created: Tue May 21 15:56:42 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setAutoFillBackground(True)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Som = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Som.sizePolicy().hasHeightForWidth())
        self.Som.setSizePolicy(sizePolicy)
        self.Som.setSizeIncrement(QtCore.QSize(1, 1))
        self.Som.setBaseSize(QtCore.QSize(1, 1))
        self.Som.setAutoFillBackground(True)
        self.Som.setObjectName("Som")
        self.gridLayout = QtWidgets.QGridLayout(self.Som)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.propertyLabel = QtWidgets.QLabel(self.Som)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propertyLabel.sizePolicy().hasHeightForWidth())
        self.propertyLabel.setSizePolicy(sizePolicy)
        self.propertyLabel.setObjectName("propertyLabel")
        self.gridLayout.addWidget(self.propertyLabel, 0, 1, 1, 1)
        self.SOMWidget = QtWidgets.QWidget(self.Som)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOMWidget.sizePolicy().hasHeightForWidth())
        self.SOMWidget.setSizePolicy(sizePolicy)
        self.SOMWidget.setAutoFillBackground(True)
        self.SOMWidget.setObjectName("SOMWidget")
        self.gridLayout.addWidget(self.SOMWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.Som)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 19))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtWidgets.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menuShow = QtWidgets.QMenu(self.menuBar)
        self.menuShow.setObjectName("menuShow")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionShowNearest = QtWidgets.QAction(MainWindow)
        self.actionShowNearest.setObjectName("actionShowNearest")
        self.actionChange = QtWidgets.QAction(MainWindow)
        self.actionChange.setObjectName("actionChange")
        self.actionAddLabels = QtWidgets.QAction(MainWindow)
        self.actionAddLabels.setObjectName("actionAddLabels")
        self.actionRemoveLabels = QtWidgets.QAction(MainWindow)
        self.actionRemoveLabels.setObjectName("actionRemoveLabels")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionTrainingData = QtWidgets.QAction(MainWindow)
        self.actionTrainingData.setObjectName("actionTrainingData")
        self.actionNewNetwork = QtWidgets.QAction(MainWindow)
        self.actionNewNetwork.setObjectName("actionNewNetwork")
        self.actionDrawUMatrix = QtWidgets.QAction(MainWindow)
        self.actionDrawUMatrix.setCheckable(True)
        self.actionDrawUMatrix.setObjectName("actionDrawUMatrix")
        self.actionWriteImage = QtWidgets.QAction(MainWindow)
        self.actionWriteImage.setObjectName("actionWriteImage")
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionLoad)
        self.menu_File.addAction(self.actionWriteImage)
        self.menu_File.addAction(self.actionQuit)
        self.menuShow.addAction(self.actionTrainingData)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menuShow.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTrain)
        self.toolBar.addAction(self.actionShowNearest)
        self.toolBar.addAction(self.actionChange)
        self.toolBar.addAction(self.actionDrawUMatrix)
        self.toolBar.addAction(self.actionAddLabels)
        self.toolBar.addAction(self.actionRemoveLabels)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewNetwork)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "SOM", None, -1))
        self.propertyLabel.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menuShow.setTitle(QtWidgets.QApplication.translate("MainWindow", "Show", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "&Training data loader", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.actionTrain.setText(QtWidgets.QApplication.translate("MainWindow", "Train", None, -1))
        self.actionShowNearest.setText(QtWidgets.QApplication.translate("MainWindow", "Show nearest", None, -1))
        self.actionChange.setText(QtWidgets.QApplication.translate("MainWindow", "Change property", None, -1))
        self.actionAddLabels.setText(QtWidgets.QApplication.translate("MainWindow", "Add labels", None, -1))
        self.actionRemoveLabels.setText(QtWidgets.QApplication.translate("MainWindow", "Remove Labels", None, -1))
        self.actionLoad.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.actionTrainingData.setText(QtWidgets.QApplication.translate("MainWindow", "TrainingData", None, -1))
        self.actionNewNetwork.setText(QtWidgets.QApplication.translate("MainWindow", "New network", None, -1))
        self.actionDrawUMatrix.setText(QtWidgets.QApplication.translate("MainWindow", "Draw U-Matrix", None, -1))
        self.actionWriteImage.setText(QtWidgets.QApplication.translate("MainWindow", "WriteImage", None, -1))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Thu Jun 30 13:57:25 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 750)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setAutoFillBackground(True)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Som = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Som.sizePolicy().hasHeightForWidth())
        self.Som.setSizePolicy(sizePolicy)
        self.Som.setSizeIncrement(QtCore.QSize(1, 1))
        self.Som.setBaseSize(QtCore.QSize(1, 1))
        self.Som.setAutoFillBackground(True)
        self.Som.setObjectName("Som")
        self.gridLayout = QtGui.QGridLayout(self.Som)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.propertyLabel = QtGui.QLabel(self.Som)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propertyLabel.sizePolicy().hasHeightForWidth())
        self.propertyLabel.setSizePolicy(sizePolicy)
        self.propertyLabel.setObjectName("propertyLabel")
        self.gridLayout.addWidget(self.propertyLabel, 0, 1, 1, 1)
        self.SOMWidget = QtGui.QWidget(self.Som)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOMWidget.sizePolicy().hasHeightForWidth())
        self.SOMWidget.setSizePolicy(sizePolicy)
        self.SOMWidget.setAutoFillBackground(True)
        self.SOMWidget.setObjectName("SOMWidget")
        self.gridLayout.addWidget(self.SOMWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.Som)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 19))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menuShow = QtGui.QMenu(self.menuBar)
        self.menuShow.setObjectName("menuShow")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTrain = QtGui.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionShowNearest = QtGui.QAction(MainWindow)
        self.actionShowNearest.setObjectName("actionShowNearest")
        self.actionChange = QtGui.QAction(MainWindow)
        self.actionChange.setObjectName("actionChange")
        self.actionAddLabels = QtGui.QAction(MainWindow)
        self.actionAddLabels.setObjectName("actionAddLabels")
        self.actionRemoveLabels = QtGui.QAction(MainWindow)
        self.actionRemoveLabels.setObjectName("actionRemoveLabels")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionTrainingData = QtGui.QAction(MainWindow)
        self.actionTrainingData.setObjectName("actionTrainingData")
        self.actionNewNetwork = QtGui.QAction(MainWindow)
        self.actionNewNetwork.setObjectName("actionNewNetwork")
        self.actionDrawUMatrix = QtGui.QAction(MainWindow)
        self.actionDrawUMatrix.setCheckable(True)
        self.actionDrawUMatrix.setObjectName("actionDrawUMatrix")
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionLoad)
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SOM", None, QtGui.QApplication.UnicodeUTF8))
        self.propertyLabel.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuShow.setTitle(QtGui.QApplication.translate("MainWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Training data loader", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrain.setText(QtGui.QApplication.translate("MainWindow", "Train", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowNearest.setText(QtGui.QApplication.translate("MainWindow", "Show nearest", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChange.setText(QtGui.QApplication.translate("MainWindow", "Change property", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLabels.setText(QtGui.QApplication.translate("MainWindow", "Add labels", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveLabels.setText(QtGui.QApplication.translate("MainWindow", "Remove Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrainingData.setText(QtGui.QApplication.translate("MainWindow", "TrainingData", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewNetwork.setText(QtGui.QApplication.translate("MainWindow", "New network", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDrawUMatrix.setText(QtGui.QApplication.translate("MainWindow", "Draw U-Matrix", None, QtGui.QApplication.UnicodeUTF8))

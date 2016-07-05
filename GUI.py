"""Module for graphical user interface"""
from PySide.QtGui import *
from PySide.QtCore import *
import pyexcel

import trainingDataLoaderUi
import trainingDataWindowUi
import mainWindowUi
import SOMDialogUi


class SOMTrainigDataLoader(QMainWindow):
    """Reads data from exel file and"""
    def __init__(self, parent=None):    
        QMainWindow.__init__( self, parent )      
        self.ui = trainingDataLoaderUi.Ui_TrainingDataLoader()
        self.ui.setupUi( self )   
    
    def readFile(self, pathToFile):
        self.ui.Data.clear()
        self.ui.Data.setColumnCount(0)
        self.ui.Data.setRowCount(0)
        
        table=pyexcel.get_array(file_name=pathToFile)        
              
        for i,row in enumerate(table):
            self.ui.Data.insertRow(i)
            for j, cell in enumerate(row):                        
                if(j>=self.ui.Data.columnCount()):
                    #Add columns if readed tablses row has more column than 
                    #tablewidget
                    self.ui.Data.insertColumn(j)
                self.ui.Data.setItem(i,j,QTableWidgetItem(str(cell)))
        self.show()  


class UI (QMainWindow):
    """Main UI class creates other UI objects"""
    def __init__(self,data ):

        QMainWindow.__init__(self )      
        self.ui=mainWindowUi.Ui_MainWindow()
        self.ui.setupUi( self )      
        self.trainingDataUi = trainingDataWindowUi.Ui_trainingDataWin() 
        self.ui.trainWindow=QMainWindow()
        self.trainingDataUi.setupUi(self.ui.trainWindow)       
         
        self.networkInitialiserUi=SOMDialogUi.Ui_SomInit()
        self.ui.networkInitDialog=QDialog(self)
        self.networkInitialiserUi.setupUi(self.ui.networkInitDialog)
        
        self.ui.trainingData=self.trainingDataUi.trainingData
        self.ui.trainWindow.setCentralWidget( self.ui.trainingData)
        self.ui.trainingData.setRowCount(len(data))
        self.ui.trainingData.setColumnCount(len(data[0]))
        self.ui.trainingDataLoader=SOMTrainigDataLoader(self)

        #Create nearest select dialog
        self.nearDialog=self.createNearestSelectDialog(data) 
        #Create train dialog
        self.trainingDialog = self.createTrainingDialog()
        
        self.Som=self.ui.Som
        self.SOMWidget=self.ui.SOMWidget
        self.trainingData=self.ui.trainingData
        self.actionTrain=self.ui.actionTrain
        self.actionChange=self.ui.actionChange
        self.actionShowNearest=self.ui.actionShowNearest
        self.trainingDataLoader=self.ui.trainingDataLoader
        self.actionAddLabels=self.ui.actionAddLabels
        self.actionSave=self.ui.actionSave
        self.actionLoad=self.ui.actionLoad
        self.actionTrainingData=self.ui.actionTrainingData
        self.actionRemoveLabels=self.ui.actionRemoveLabels
        self.actionNewNetwork=self.ui.actionNewNetwork
        self.networkInitDialog=self.ui.networkInitDialog
        self.actionLoadTrainingData=self.trainingDataUi.actionLoad
        self.propertyLabel=self.ui.propertyLabel      
        self.trainWindow=self.ui.trainWindow
        self.actionDrawUMatrix=self.ui.actionDrawUMatrix
        
        
    def createNearestSelectDialog(self,data):
        nearDialog = QDialog(self)
        nearLayout=QVBoxLayout(nearDialog)        
        self.nearTable=QTableWidget(nearDialog)
        self.nearTable.setRowCount(1)
        self.createNearestDialog(len(data[0]))           
        nearButtons=QDialogButtonBox(nearDialog)
        nearOK=QPushButton(nearButtons)
        nearOK.setText("OK")
        nearOK.clicked.connect(lambda: self.showNearest())
        nearCancel=QPushButton(nearButtons)
        nearCancel.setText("Cancel")
        nearCancel.clicked.connect(lambda: nearDialog.reject())
        nearButtons.addButton(nearOK,QDialogButtonBox.AcceptRole)
        nearButtons.addButton(nearCancel,QDialogButtonBox.RejectRole)
        nearButtons.show()   
        nearLayout.addWidget(self.nearTable)
        nearLayout.addWidget(nearButtons)
        nearDialog.setSizeGripEnabled(True)
        return nearDialog

    def createTrainingDialog(self):
        trainDialog=QDialog(self)
        trainLayout=QVBoxLayout(trainDialog)
        self.trainSpinBox=QSpinBox(trainDialog)
        self.trainSpinBox.setMaximum(1000000)
        self.trainSpinBox.setMinimum(200)
        self.trainSpinBox.setValue(500)
        self.trainPropBox=QWidget(trainDialog) 
        self.trainPropBoxLayot=QHBoxLayout(self.trainPropBox)
        self.trainPropList=[]
        self.createTrainPropertyBox(self.ui.trainingData.columnCount(),False)           
        self.trainButtons=QDialogButtonBox (QDialogButtonBox.Ok
                                      | QDialogButtonBox.Cancel ,
                                      parent=trainDialog)    
        trainLayout.addWidget(self.trainPropBox)
        trainLayout.addWidget(self.trainSpinBox)
        trainLayout.addWidget(self.trainButtons)                              
        self.trainButtons.accepted.connect(trainDialog.accept)
        self.trainButtons.rejected.connect(trainDialog.reject)                              
        return trainDialog 

         
    def createTrainPropertyBox(self, dataSize, header=False):
        """Clears properties from train dialgo and adds new ones"""
        while self.trainPropBoxLayot.count()>0:
            item=self.trainPropBoxLayot.takeAt(0)
            if not item:
                continue
            w=item.widget()
            w.deleteLater()  
            
        for i in range( dataSize):
            print (i)
            chekBox= QCheckBox()
            if(header):            
                chekBox.setText(
                            self.trainingData.horizontalHeaderItem(i).text())
            else:
                chekBox.setText(str(i+1))   
            self.trainPropBoxLayot.addWidget(chekBox)
            self.trainPropList.append(QCheckBox(chekBox))    
    
    def createNearestDialog(self, dataSize, headers=[]):
        self.nearTable.setColumnCount(dataSize)
        if(headers):
            self.nearTable.setHorizontalHeaderLabels(headers)
            self.SOMWidget.setPropertyLabels(headers)
    
    def TrainDialog(self):
        self.trainingDialog.show()
        self.trainingDialog.raise_()
        self.trainingDialog.activateWindow()
     
    def showNearest(self):
        tmpstr=""
        for i in range(self.nearTable.columnCount()): 
            tmpstr+=self.nearTable.item(0,i).text()+", "
        tmpstr=tmpstr[:len(tmpstr)-2]
        self.SOMWidget.highlightNearest(tmpstr)
        
    
    
    #Set selected items values to nearestDialog
    def nearestSelect(self, row, col):
        """Slot gfor setting data from row to nearest dialog."""
        for i in range(self.ui.trainingData.columnCount()):
            #Create new QTableWidgetItem because QTableWidgetItems cannot be 
            #in several different tables
            self.nearTable.setItem(0, i, QTableWidgetItem( 
                                      self.ui.trainingData.item(row,i)))
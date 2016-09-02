"""
Main module, handles communication between GUI and SOM
"""
from PySide.QtCore import *
from PySide.QtGui import *

import sys
import _thread
from sklearn.datasets.samples_generator import make_blobs
#from sklearn import datasets

from som import SOM
from GUI import UI
from SOMVisualizer import SOMVisualizer


class PyQtSOM (  ):

    def __init__ ( self, parent = None ):     
        #Generate example training data        
        centers= [
                 [1,1,1,1,1], 
                 [5,5,5,1,1], 
                 [1,1,1,5,5], 
                 [3,3,3,3,3], 
                 [1,2,3,4,5], 
                 [5,4,3,2,1]
                 ]
        data, labels_true = make_blobs(n_samples=300,n_features=5, 
                                       centers=centers, cluster_std=1,
                                       random_state=0)    
        self.ui=UI(data) #Ui object creates GUI for aplication
        fillTableWidget(data,self.ui.trainingData)         
        self.som=SOM(vectorSize=len(data[0]),width=25,height=25)
        
        #Randomize SOM with minimun and maximum values taken from training data
        self.som.randomize(data)
        self.ui.SOMWidget=SOMVisualizer(window=self.ui.Som,
                                            train=data,som=self.som)  

              
        #Connect signals to slots
        self.ui.nearDialog.rejected.connect(self.ui.SOMWidget.toggleNearest)
        self.ui.actionTrain.triggered.connect(self.ui.trainingDialog.show)
        self.ui.actionChange.triggered.connect(
                                lambda: self.ui.SOMWidget.change())
        self.ui.actionShowNearest.triggered.connect(self.ui.nearDialog.show)
        self.ui.trainingData.cellClicked.connect(self.ui.nearestSelect)
        self.ui.actionLoadTrainingData.triggered.connect(self.loadTrainingData)
        self.ui.trainingDataLoader.ui.actionLoad.triggered.connect(
                                self.setTrainingData)
        self.ui.actionAddLabels.triggered.connect(self.addLabels) 
        self.ui.actionSave.triggered.connect(self.saveNetwork)
        self.ui.actionLoad.triggered.connect(self.loadNetwork)     
        self.ui.propertyLabel.setText("")    
        self.ui.actionChange.triggered.connect(self.updatePropLabel)
        self.ui.actionTrainingData.triggered.connect(self.ui.trainWindow.show)
        self.ui.actionRemoveLabels.triggered.connect(
                                self.ui.SOMWidget.removeLabels)
        self.ui.actionNewNetwork.triggered.connect(
                                self.ui.networkInitDialog.open)
        self.ui.networkInitDialog.accepted.connect(self.initNetwork)
        self.ui.trainButtons.accepted.connect(lambda: 
                                self.train(self.ui.trainSpinBox.value(),data))  
                            
        self.ui.actionDrawUMatrix.triggered.connect(
                                self.ui.SOMWidget.generateUMatrix)
        self.updatePropLabel()

    def __del__ ( self ):
        self.ui = None
 
    def train(self, iterations, trainingData):
        """Gets indexes of training properties 
            and starts SOM training in new thread """
        ind=[]
        for i, checkBox in enumerate( self.ui.trainPropList):
            if checkBox.isChecked():
                ind.append(i)
        data=self.getTrainingData()
        self.som.setTrainIndexes(ind)
        _thread.start_new_thread( self.som.train,(data,iterations))
        self.ui.SOMWidget.repaint()
        
    def loadTrainingData(self):
        """Opens- QFileDialog for loading training data from file"""
        file=QFileDialog.getOpenFileName(self.ui,
                "Select file containing training data",'.',("Spreadsheets \
                (*.ods *.xls *xlsx  *.csv *.csvz *.tsv *svz *.gnumeric)"))
        self.ui.trainingDataLoader.readFile(file[0])
    

    def setTrainingData(self):
        """Sets data selected in trainingData loader as training data"""
        
        ranges=self.ui.trainingDataLoader.ui.Data.selectedRanges()
        header=self.ui.trainingDataLoader.ui.actionHeaders.isChecked()
        label=self.ui.trainingDataLoader.ui.actionLabels.isChecked()
        transpose=self.ui.trainingDataLoader.ui.actionTranspose.isChecked()                
        newNetwork=self.ui.trainingDataLoader.ui.actionInitNetwork.isChecked()        
        
        #clear previos training data
        self.ui.trainingData.clear()  
        self.ui.trainingData.setRowCount(0)  
        columnCount=ranges[0].columnCount()
        #labels should be in first column        
        if(label):
            columnCount-=1
        self.ui.trainingData.setColumnCount(columnCount)  
        i=0
        data=[]
        labels=[]
        headers=[]
        firstRange=True
        headerRow=True
        #Selection can be in multiple pieces       
        for r in ranges:
            for row in range(r.rowCount()):
                #Data headers should be in first row of the first selected area
                #For each non header row add new list to data table and new row
                #to trainingDatawidget
                if not (header and (row==0) and firstRange):
                    data.append([])               
                    headerRow=False                               
                for col in range(r.columnCount()):                           
                    item=self.ui.trainingDataLoader.ui.Data.item(r.topRow()+row,
                                                r.leftColumn()+col  )
                    if(item):
                        item=item.text()
                    if headerRow:
                        headers.append(item)                            
                    #data should be numeric or label
                    elif (isNumber(item)) or (label and col==0):
                        if(isNumber(item)):
                            item=float(item)
                        data[i].append((item))
                if not headerRow: 
                    i+=1   
            firstRange=False            
        
        #remove rows that are shorter than logest row from data table
        data=stripTable(data)
        if label:
            labels=[s.pop(0) for s in data]
            self.ui.trainingData.setRowCount(i)
        if header:     
            if label:
                headers=headers[1:] 
        #transpose data
        if(transpose):
            self.ui.trainingData.setColumnCount(len(labels))
            self.ui.trainingData.setRowCount(len(headers))
            self.ui.trainingData.setVerticalHeaderLabels(headers)
            self.ui.trainingData.setHorizontalHeaderLabels(labels)
            data=list( [list(i) for i in zip(*data)])
        else:
            self.ui.trainingData.setVerticalHeaderLabels(labels)
            self.ui.trainingData.setHorizontalHeaderLabels(headers)

        columnCount=len(data[0])
        fillTableWidget(data,self.ui.trainingData)
        self.ui.trainPropList.clear()
        self.ui.createTrainPropertyBox(columnCount,header)
        self.ui.createNearestDialog(columnCount,headers[1:])            
        if(newNetwork):
            self.ui.networkInitDialog.open()
    
  
    def addLabels(self):  
        """Labels network nodes with labels from training data"""
        ranges=self.ui.trainingData.selectedRanges()                
        labels=[]
        data=[]
        #If user has selected rows from training data
        if ranges:        
            for r in ranges:
                topRow=r.topRow()
                for row in range(r.rowCount()):
                    data.append([])
                    label=self.ui.trainingData.verticalHeaderItem(
                                                        r.topRow()+row)
                    if (label is not None):
                        labels.append(label.text())
                    else:
                        #If there are no labels use numerical index
                        labels.append(str(topRow+row+1))
                    for col in range(self.ui.trainingData.columnCount()):
                        data[len(data)-1].append(float(
                            self.ui.trainingData.item(topRow+row,col).text()))
        else:
            for i in range(self.ui.trainingData.rowCount()):
                data.append([])        
                label=self.ui.trainingData.verticalHeaderItem(i)
                if (label is not None):
                    labels.append(label.text())
                else:
                #If there are no labels use numerical index that starts
                    labels.append(str(i+1))
                for j in range(self.ui.trainingData.columnCount()):
                    data[i].append(float(
                                    self.ui.trainingData.item(i,j).text()))
        self.ui.SOMWidget.addDataLabels(data,labels)
 
    def saveNetwork(self):
        """Opens QFileDialog and calls SOMs save function"""
        file=QFileDialog.getSaveFileName(self.ui,"Select target file")
        self.som.save(file[0])
    def loadNetwork(self):
        """Opens QFileDialog and calls SOMs load function"""
        file=QFileDialog.getOpenFileName(self.ui,"Select file")
        self.som.load(file[0])
    
    #Change propertylabels text
    def updatePropLabel(self):
        """Updates property label to match property used in coloring the SOM 
        """
        item=self.ui.trainingData.horizontalHeaderItem(
                                        self.ui.SOMWidget.propertyIndex)        
        label="Property: "
        if item is None:
            #If data doesn't have labels use numerical index
            label += str(self.ui.SOMWidget.propertyIndex+1)
        else:
            label += item.text()
        self.ui.propertyLabel.setText(label)
        
        
    def initNetwork(self):
        """Inits SOM with values from networkInitDialog"""
        w=self.ui.networkInitialiserUi.widthSB.value()
        h=self.ui.networkInitialiserUi.heightSB.value()
        ts=self.ui.networkInitialiserUi.trainSpeedSB.value()                
        self.som.__init__(vectorSize=self.ui.trainingData.columnCount(), 
                          width=w, height=h,trainingSpeed=ts)
                       
        data=self.getTrainingData()
        self.som.randomize(data)
    
    def getTrainingData(self):
        """Return 2d data array generated from QTableWidget"""
        data=[] 
        for i in range(self.ui.trainingData.rowCount()):
            data.append([])            
            for j in range(self.ui.trainingData.columnCount()):
                data[i].append(float( self.ui.trainingData.item(i,j).text()))
        return data

def isNumber(s):
    """Checks if s is number"""
    if s is None:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def fillTableWidget(array,widget):
    """Fills given QTableWidget with data from array"""
    widget.setRowCount(len(array))
    widget.setColumnCount(len(array[0]))
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            widget.setItem(i,j,QTableWidgetItem(str(col)))
    return widget

#Remove table rows that are shorter than longest row to remove jaggedness
def stripTable(table):
    """Removes table rows that are shorter than longest row in table"""
    a=max(map(len,table))
    i=0
    while(i<len(table)):
        if len(table[i])<a:
            table.pop(i)
        else:
            i+=1
    return table
  
    
if __name__ == '__main__':
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'python SOM' )
    # create widget
    w = PyQtSOM()
    w.ui.setWindowTitle( 'Python SOM' )
    w.ui.show()
    w.ui.SOMWidget.repaint()
    # connection
    QObject.connect( app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))
    # execute application
    sys.exit( app.exec_() )
    
    
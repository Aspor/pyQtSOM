import numpy as np
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSvg import *

import som

class SOMVisualizer(QWidget):
    """Widget for painting the SOM"""
    def __init__(self, window, train,som):
        self.som=som #SOM object        
        self.propertyLabels=[] #Labels from training data headers      
        self.dataLabels=[] #Category labels
        self.nearest=makeHexagon(0,0,0,0) 
        self.nearestBool=False #Should nearest node be highligthed       
        self.par=window #For proper resizing
        QWidget.__init__(self,window)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        self.h=self.height()/len(self.som.map) #height of single node
        self.w=self.width()/len(self.som.map[0]) #width of sigle node
        self.propertyIndex=0 #Property for coloring scheme
        
        self.UMatrix=[]        
        self.drawUMatrix=False
        
    def paintEvent(self, event):
        
        painter = QPainter()
        painter.begin(self)
        self.paint(painter)           
        painter.end()
        
    def setPropertyLabels(self, labels=[]):
        self.propertyLabels=labels
    
    def addDataLabels(self, data,labels):
        """Add labels to corresponding nodes"""
        self.removeLabels()          
        data=som.normalize(data)
        w=self.w
        h=self.h
        for i,dat in enumerate(data):
            nearest=self.som.nearestNeigbor(dat)              
            x= w*nearest[1]*0.75
            y= 0.4*h + h*nearest[0]+nearest[0]%2*h*0.5
            lab=(labels[i])
            arr=[x,y,lab]            
            self.dataLabels.append(arr)

 
    def removeLabels(self):
        self.dataLabels.clear()


    def drawNearest(self,j,i):
        w=self.w
        h=self.h        
        self.nearest=makeHexagon(0.25*w-2 + w*i*0.75, 0.25*h + h*j+i%2*h*0.5-2
                                ,w/2.0+4,h/2.0+4)
        self.repaint()


    def highlightNearest(self,data):
        """Finds nearest neighbor to given data and sets it to be drawn"""
        self.nearestBool=True
        dataArr= [float(s) for s in data.split(',')]
        ind=self.som.nearestNeigbor(dataPoint=dataArr)
        self.drawNearest(ind[0],ind[1])

    def toggleNearest(self):
        """Stop drawing nearest neighbor"""
        self.nearestBool= False
        self.repaint()
        
    def change(self):
        """Change property used for painting"""
        self.propertyIndex+=1
        if(self.propertyIndex>=len(self.som.map[0][0])):
            self.propertyIndex=0            
        self.repaint()

    
    def generateUMatrix(self):
        """Togles U-Matrix drawing and if necessary generates UMatrix"""
        if not self.drawUMatrix:
            UMatrix=[]
            #For every node in network
            for j, col in enumerate( self.som.map):
                UMatrix.append([])
                for i, node in enumerate (col):
                    dist=0
                    for ind in som.inRange(i,j,1):
                        #If neighboring node is inside the SOM
                        if((ind[0]>=0)and(ind[1]>=0) and
                          (ind[0]<self.som.height) and
                          (ind[1]<self.som.width)):
                            for m in range (len(node)):
                                dist+=pow( (node[m]-
                                    self.som.map[ind[1]][ind[0]][m]),2)
                    UMatrix[j].append(pow(dist,0.5))
            self.UMatrix=UMatrix
            self.drawUMatrix=True
        else:
            self.drawUMatrix=False
    
    def save(self):
        file=QFileDialog.getSaveFileName(unicode="nameForFile")
        filename=file[0]
        if len(filename)==0:
            return;
        generator=QSvgGenerator()
        generator.setFileName(filename)
      #  generator.setSize(200, 200)
#        generator.setSize(QSize(200, 200))
        
#        generator.setViewBox( (0, 0, 200, 200))             
        generator.setTitle(("SVG Generator Example Drawing"))
        generator.setDescription(("An SVG drawing created by the SVG Generator Example provided with Qt."))
        painter=QPainter()
        painter.begin(generator)
        self.paint(painter)
        painter.end()
        print("saved"+filename)
        
    def paint(self, painter):
        
        self.resize(self.par.size())
      #  self.resize(self.width() ,self.height())
        self.h=self.height() / len(self.som.map)
        self.w=self.width()/len(self.som.map[0])
        h=self.h
        w=self.w
        
        
        #Max and min values from SOM for property used in coloring
        netMax=0
        netMin=0
        if self.drawUMatrix:
            netMax=np.amax( self.UMatrix)
            netMin=np.amin( self.UMatrix)
        else:
            netMax=np.amax(self.som.map,axis=(0,1))[self.propertyIndex].item()  
            netMin=np.amin(self.som.map,axis=(0,1))[self.propertyIndex].item()  
        for j, col in enumerate(self.som.map):
            for i, node in enumerate(col):

                #Value should be between 0 and 255 and increase lineary
                val=0
                if self.drawUMatrix:    
                    val=(self.UMatrix[j][i]-netMin)*255/(netMax-netMin)
                else:
                    val=255/(netMax-netMin)*(node[self.propertyIndex]-netMin)
                
                c=QColor(val,0,255-val)        
                brush=QBrush(c)
                
                #Create hexagon with proper tiling. Add some padding 
                poly=makeHexagon(0.25*w-2 + w*i*0.75, 0.25*h + h*j+i%2*h*0.5-2,
                                 w/1.8+2,h/1.8+2)
                path=QPainterPath()
                path.addPolygon(poly)
                painter.fillPath(path,brush)
                #painter.drawText( w*i*0.75-12, h*j+i%2*h*0.5+6, str( (i,j) ) )
                
                if(self.nearestBool):                
                    path2=QPainterPath()                
                    path2.addPolygon(self.nearest)                
                    painter.fillPath(path2,Qt.cyan)            
        for label in self.dataLabels:
            painter.drawText(label[0],label[1],label[2])
            


def makeHexagon(x,y,w,h):
    """Return hexagonal QPolygon. (x,y) is top left coner"""
    points=[]
    cos=[1.,0.5,-0.5,-1,-0.5,0.5]
    sin=[0,0.866025,0.866025,0,-0.866025,-0.866025]    
    for i in range(len (cos)):
        points.append(QPoint(x+w*cos[i],y+h*sin[i]))
    return QPolygonF(points)  
    

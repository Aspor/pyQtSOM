"""Simple SOM implementation. Uses planar map with hexagonal tiling"""

from random import randint, uniform, seed
import numpy as np
from enum import IntEnum
import time
from PySide2.QtCore import QObject, Slot, Signal, QThread

class trainingModes(IntEnum):
        NORMAL = 0
        BATCH = 1

class SOM(QThread):
    def __init__(self, vectorSize=0, width=25, height=25, trainingSpeed=0.5):
        super(SOM, self).__init__()    
        seed()
        self.trainingMode = trainingModes.NORMAL;
        self.init(vectorSize,width,height,trainingSpeed);
        self.trainingData = [[]]
        self.iteratons = 200
        self.trainingSpeed = 0.5
        self.neigborhoodSize=3
        
    trainingDone = Signal();

    def init(self, vectorSize=0, width=25, height=25, trainingSpeed=0.5):
        self.dataSize = vectorSize
        self.width = width
        self.height = height
        self.map = [[[ uniform(1,-1) for i in range(vectorSize) ] for j in range( height) ] for k in range (width)]
        self.randomize()
#        print (self.map.shape,"INIT")
        self.trainingSpeed = trainingSpeed
        #Properties used for training
        self.trainIndexes = []
        self.stop = False;
        self.rangeArray=[[ dict()  for j in range( height) ] for k in range (width)]
        self.distArray = [[[[-1]*height]*width]*height]*width
        self.gaussianArray=[[]]

        self.dataMin=[]
        self.dataMax=[]
     
    def run(self):    
        if self.trainingMode==trainingModes.BATCH:
            self.batchTrain(self.trainingData,self.iteratons,self.neigborhoodSize)
        elif self.trainingMode==trainingModes.NORMAL:
            self.iterativeTrain(self.trainingData ,self.iteratons,self.trainingSpeed,self.neigborhoodSize)
        print("Trained")
        self.trainingDone.emit()
        
    def train(self, trainingData = [[]],iteratons=1000,trainingSpeed=0.5,neigborhoodSize=3):
        self.trainingData, self.dataMax, self.dataMin = normalize(trainingData)
        self.iteratons = iteratons
        self.trainingSpeed = trainingSpeed
        self.neigborhoodSize=neigborhoodSize
        self.gaussianArray = [[0]*(neigborhoodSize+1)]*(neigborhoodSize+1)
               
    def iterativeTrain(self, trainingData = [[]],iteratons=1000,trainingSpeed=0.5,neigborhoodSize=3):
          """Selects nodes randomly from training data and adjust map with it"""
          for i in range (iteratons):
              if self.stop:
                  self.stop = False
                  break
              time.sleep(0.00001)
              ind=randint(0,len(trainingData)-1)
              neighbor=self.nearestNeigbor(trainingData[ind],True)
              self.adjustNet(np.array(trainingData[ind]), neighbor[0],
                                        neighbor[1],self.trainingSpeed,neigborhoodSize )
              #trainig speed slows with every iteration.
              trainingSpeed=trainingSpeed*0.999 
                
    def adjustNet(self, data,BMU_i, BMU_j,trainingSpeed, neigborhoodSize):
        """Finds adjusts hit node and its neighbours """
        #Cast target data to numpy arary for vector operations
        data=np.array(data)
        try: self.rangeArray[BMU_i][BMU_j][neigborhoodSize]==True
        except KeyError: self.rangeArray[BMU_i][BMU_j][neigborhoodSize] = inRange(BMU_i,BMU_j,neigborhoodSize)
        for ind in self.rangeArray[BMU_i][BMU_j][neigborhoodSize]:
            if((ind[0]>=0)and(ind[1]>=0) and
              (ind[0]<self.width) and (ind[1]<self.height)):
                    node= np.array(self.map[ind[0]][ind[1]])
                    #futher node is from the winner, less we change its values                    
                    weight= self.gaussian([BMU_i,BMU_j],ind, neigborhoodSize)
                    self.map[ind[0]][ind[1]] = (node +  trainingSpeed 
                                            *(data - node)*weight)
                         
    def nearestNeigbor(self, dataPoint=[],normalized=False):
        """Finds closest match to data Point"""
        nearest=[]
        shortestDist=-1
        first=True        
        if (not normalized):
            dataPoint=normalizeVector(dataPoint,self.dataMax,self.dataMin)
        #User can exclude some properties from training to find hidden 
        #depencies
        if len(self.trainIndexes):
            #Iterate whole network
            for i, column in enumerate(self.map):
                for j, node in enumerate(column):
                    dist=0    
                    for a in self.trainIndexes:
                        dist+= (dataPoint[a] - node[a])**2
                    
                    #We set distance as distance from first node 
                    if(dist < shortestDist) or first:
                        shortestDist=dist
                        first=False
                        nearest=[i,j]           
        else:
            for i, column in enumerate(self.map):
                for j, node in enumerate(column):
                    dist=0    
                    for a,d in enumerate(dataPoint):
                        dist+= (dataPoint[a] - node[a])**2
                    if(dist < shortestDist) or first:                           
                        shortestDist=dist
                        first=False
                        nearest=[i,j]
        return nearest
        
    def randomize(self, max=1, min=-1 ):
        """Randomizes network with values between maximun
        and minimun values from training data"""
        self.map = [ [ [ uniform(max,min) for i in range(self.dataSize) ] for j in range( self.height) ] for k in range (self.width)]

    def setTrainIndexes(self, ind=[]):
        print (ind)
        self.trainIndexes=ind
    
    def save(self, file):
        """Writes network to file"""
        f=open(file, 'w')
        f.write(str(self.map.shape )+ '\n')
        for row in self.map:
            for col in row:
                #default max line widht is way too short and we want write
                #one node per line
                f.write(np.array_str(col,max_line_width=9999999999999999999))                
                f.write(' \n')
    
    def load(self, file):
        """Reads network from file"""
        f=open(file,'r')
        lines=f.readlines()
        shape=lines[0].split(',')              
        #self.width=int(shape[0][1:])
        #self.height=int(shape[1])
        self.width=int(shape[0][1:])
        self.height=int(shape[1])
        
        self.dataSize=int(shape[2][:-2])
        self.map=np.zeros((self.width,self.height,self.dataSize))

        for i, line in enumerate(lines[1:]):
            dataVec=line.split()
            node=[]
            for n in dataVec:
                tmpStr=n.strip('[ ]')
                if tmpStr:                
                    node.append(float(tmpStr))                    
            self.map[int(i/self.height)][i%self.height]=node
        print(self.map.shape,"LOAD")
        
    def batchTrain(self, trainingData,iterations,neighborhoodSize):
        prototypeSum=np.zeros((self.width,self.height,self.dataSize))
        size=neighborhoodSize
        prototypeDiv=np.zeros((self.width,self.height))
        
        for t in range(iterations): 
            if self.stop:
                self.stop = False
                break;
            for data in trainingData:
                data=np.array(data)
                neighb=self.nearestNeigbor(data,True)
                try: self.rangeArray[neighb[0]][neighb[1]][size]==True
                except KeyError: self.rangeArray[neighb[0]][neighb[1]][size] = inRange(neighb[0],neighb[1],size)

                for node in self.rangeArray[neighb[0]][neighb[1]][size]:
                    if((node[0]>=0)and(node[1]>=0) and
                    (node[0]<self.width) and (node[1]<self.height)):
                        gaus =self.gaussian(node,neighb,size,1)
                        prototypeSum[node[0]][node[1]]+=data*gaus
                        prototypeDiv[node[0]][node[1]]+=gaus
            size=neighborhoodSize - int((t/iterations)*neighborhoodSize)
            for i, column in enumerate(self.map):
                for j, node in enumerate(column):
                    for m in range(self.dataSize):
                        if prototypeDiv[i][j]!=0:
                            prototypeSum[i][j][m]=prototypeSum[i][j][m]/prototypeDiv[i][j]
            print(t,iterations, "t,Iter" ,size,neighborhoodSize)
            self.map=np.array(prototypeSum)
            prototypeSum=np.zeros((self.width,self.height,self.dataSize))
            prototypeDiv=np.zeros((self.width,self.height))
    
    @Slot()
    def stopTraining(self):
        self.stop=True
    
    def changeTrainingMode(self, index):
        self.trainingMode=index
    
    def hexDistance(self, node1, node2):
        if self.distArray[node1[0]][node1[1]][node2[0]][node2[1]] !=-1:
            return self.distArray[node1[0]][node1[1]][node2[0]][node2[1]]
        c1=hexToCube(node1)
        c2=hexToCube(node2)
        dist=int((abs( c1[0]-c2[0])+ abs(c1[1]-c2[1])+abs (c1[2]-c2[2]))/2)
        self.distArray[node1[0]][node1[1]][node2[0]][node2[1]]=dist
        
        print(node1,node2,dist)
        return  dist
        
    def gaussian(self, pos,center,width=2,height=1):
        dist=self.hexDistance(pos,center)
       # print(dist,width,self.neigborhoodSize)
        if(self.gaussianArray[dist-1][width-1]):
            return height*self.gaussianArray[dist-1][width-1]
        e=np.e
        c2=2*width**2
        self.gaussianArray[dist-1][width-1] = e**((-dist**2)/c2)
        return height*self.gaussianArray[dist-1][width-1]
        
def hexToCube(node):
    z = node[1]-(node[0]-node[0]&1)/2;
    x = node[0]
    y = -x-z
    print(x,y,z)
    return[x,y,z]

def inRange(i,j,dist):
    """Returns list of indexes of nodes in distance away of (i,j)"""
    result=set()
    #Cubical coordinates (x,y,z)
    for x in range(-dist , dist+1):
        for y in range(max(-dist,-dist-x) ,min(dist+1,dist+1-x)):
            z = -x-y
            col = x
            row = int( z + (x + (x&1)) / 2)
            result.add((i+col,j+row))
    return result
    
def normalize(data=[[]] ):
    data=np.array(data)
    netMax=np.amax(data,axis=(0))
    netMin=np.amin(data,axis=(0))
    for i,col in enumerate (data):
        for j,row in enumerate (data[i]):
            data[i][j]= normalizeValue(row,netMax[j],netMin[j])
    return data, netMax, netMin
    
def normalizeValue(val, netMax, netMin):
    r = 1-2 / (netMax - netMin) * (val-netMin)
    return r

def normalizeVector(dataVector,dataMax,dataMin):
    normalized=[0]*len(dataVector)
    #print("DATA",dataVector,dataMax,dataMin)
    for i, val in enumerate(dataVector):
        normalized[i] = normalizeValue(val,dataMax[i],dataMin[i])
    return normalized;
 
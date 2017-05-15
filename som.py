"""Simple SOM implementation. Uses planar map with hexagonal tiling"""

from random import randint, uniform
import numpy as np
import time

class SOM(object):
    def __init__(self, vectorSize=0, width=25, height=25, trainingSpeed=0.5):
        self.dataSize = vectorSize
        self.width = width
        self.height = height
        self.map = [[[0]*vectorSize]*height]*width
        self.map = np.zeros((width, height, vectorSize))
        print (self.map.shape,"INIT")
        self.trainingSpeed = trainingSpeed

        #Properties used for training
        self.trainIndexes = []

    def train(self, trainingData = [[]],iteratons=1000,trainingSpeed=0.5,neigborhoodSize=3):
#        self.batchTrain(trainingData,150,5)
    
        trainingData=normalize(trainingData)
        self.trainingSpeed=trainingSpeed        
        """Selects nodes randomly from training data and adjust map with it"""
        for i in range (iteratons):
            time.sleep(0.00001)
            ind=randint(0,len(trainingData)-1)
            neighbor=self.nearestNeigbor(trainingData[ind])
            self.adjustNet(np.array(trainingData[ind]), neighbor[0],
                                    neighbor[1],self.trainingSpeed,neigborhoodSize )
            #trainig speed slows with every iteration.
            self.trainingSpeed=self.trainingSpeed*0.999 
            
        print("Trained")
    
    def adjustNet(self, data,BMU_i, BMU_j,trainingSpeed, neigborhoodSize):
        """Finds adjusts hit node and its neighbours """
        
        #Cast target data to numpy arary for vector operations
        data=np.array(data)
    
        for ind in inRange(BMU_i,BMU_j,neigborhoodSize ):
            if((ind[0]>=0)and(ind[1]>=0) and
              (ind[0]<self.width) and (ind[1]<self.height)):
                    node= np.array(self.map[ind[0]][ind[1]])
                    #futher node is from the winner, less we change its values                    
                    weight= gaussian([BMU_i,BMU_j],ind, neigborhoodSize  )
                    self.map[ind[0]][ind[1]]= (node +  trainingSpeed 
                                            *(data - node)*weight)
                         
    def nearestNeigbor(self, dataPoint=[]):
        """Finds closest match to data Point"""
        nearest=[]
        shortestDist=-1
        first=True
        
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
        
    def randomize(self,trainingData):
        """Randomizes network with values between maximun
            and minimun values from training data"""
        trainingData=normalize(trainingData)            
            
        netMax=np.max(trainingData,axis=0)
        netMin=np.min(trainingData,axis=0)
        for col in self.map:
            for row in col:
                for i,m in enumerate(row):
                    row[i]=uniform(netMin[i],netMax[i])
    
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
            for data in trainingData:
                data=np.array(data)
                neighb=self.nearestNeigbor(data)
                for node in inRange(neighb[0],neighb[1],size):
                    if((node[0]>=0)and(node[1]>=0) and
                    (node[0]<self.width) and (node[1]<self.height)):
                        prototypeSum[node[0]][node[1]]+= data*gaussian(node,neighb,size,1)
                        prototypeDiv[node[0]][node[1]]+=gaussian(node,neighb,size,1)
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



    
def hexDistance( node1, node2):
    c1=hexToCube(node1)
    c2=hexToCube(node2)
    dist=abs( c1[0]-c2[0])+ abs(c1[1]-c2[1])+abs (c1[2]-c2[2])/2
    return dist
    
def gaussian(pos,center,width=2,height=1):
    e=np.e
    c2=2*width**2
    dist= -(hexDistance(pos,center)**2)
    return height*e**(dist/c2)
        
def hexToCube(node):
    x=node[0]-(node[1]-node[1]&1)/2;
    z = node[1]
    y=-x-z
    return[x,y,z]


def inRange(i,j,dist):
    """Returns list of indexes of nodes in distance away of (i,j)"""
    result=[]
    #Cubical coordinates (x,y,z)
    for x in range(-dist , dist+1):
        for y in range( max(-dist,-dist-x) ,min(dist+1,dist+1-x)):
            z = -x-y
            col = x
            row = int( z + (x + (x&1)) / 2)
            result.append((i+col,j+row))
    return result
    
def normalize(data=[[]] ):
    data=np.array(data)
    netMax=np.amax(data,axis=(0))
    netMin=np.amin(data,axis=(0))
    for i,col in enumerate (data):
        for j,row in enumerate(col):
            data[i][j]=1-2/(netMax[j]-netMin[j])*(data[i][j]-netMin[j])
#    print (data,np.amax(data,axis=(0)),np.amin(data,axis=(0)))
    return data
    

     

from PySteppables import *
import CompuCell
import sys
from random import randint

class CellMotionSteppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        for count in range (100):
            x = randint(0,99)
            y = randint(0,99)
            if count%2 == 0:
                self.cellField[x:x+1, y:y+1, 0] = self.newCell(self.A)
            else: 
                self.cellField[x:x+1, y:y+1, 0] = self.newCell(self.B)
        for cell in self.cellList:
            cell.targetVolume = 25.0
            cell.lambdaVolume = 10.0
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            if cell.type == 1:
                cell.lambdaVecX = -10.0
                cell.lambdaVecY = 0.0
                cell.lambdaVecZ = 0.0
            else:
                cell.lambdaVecX = 10.0
                cell.lambdaVecY = 0.0
                cell.lambdaVecZ = 0.0
    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        
from PySteppables import *
from PySteppablesExamples import MitosisSteppableBase
import CompuCell
import sys

from PlayerPython import *
from math import *


class Mitosis(MitosisSteppableBase):
    def __init__(self,_simulator,_frequency=1):
        MitosisSteppableBase.__init__(self,_simulator, _frequency)
    
    def step(self,mcs):
        # print "INSIDE Mitosis"
        cells_to_divide=[]
        for cell in self.cellList:
            if cell.volume>200:
                
                cells_to_divide.append(cell)
                
        for cell in cells_to_divide:
            # to change mitosis mode leave one of the below lines uncommented
            self.divideCellRandomOrientation(cell)
            # self.divideCellOrientationVectorBased(cell,1,0,0)                 # this is a valid option
            # self.divideCellAlongMajorAxis(cell)                               # this is a valid option
            # self.divideCellAlongMinorAxis(cell)                               # this is a valid option

    def updateAttributes(self):
        self.parentCell.targetVolume /= 2.0 # reducing parent target volume                 
        self.cloneParent2Child()            
        
        # for more control of what gets copied from parent to child use cloneAttributes function
        # self.cloneAttributes(sourceCell=self.parentCell, targetCell=self.childCell, no_clone_key_dict_list = [attrib1, attrib2] )
        
#         self.childCell.type = self.A
        
#         if self.parentCell.type==1:
#             self.childCell.type=2
#         else:
#             self.childCell.type=1
import math
import numpy
import scipy
from scipy import constants
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects import rl

r = robjects.r
r.source("./module/Rscript.R")

class obj():
    existing_objs = []

    
    def __init__(self, id, posx, posy, dx, dy, d2x, d2y):
        self.id = id
        self.posx = posx
        self.posy = posy
        self.dx = dx
        self.dy = dy
        self.d2x = d2x
        self.d2y = d2y
        obj.existing_objs.append(self)

        

    def updateObjA(self): 
        """
        calculate and update the acceleration (d2x,d2y) of an obj instance
 
        Parameters
        ----------
        self: an instance of obj
 
        Returns
        -------
        void
        """
        self.d2x = 0
        self.d2y = 0
        
        #get a list of all other objs
        other_objs = list(obj.existing_objs)
        other_objs.remove(self)
        
        #add the acceleration due to gravitation of every other obj to self.d2x/d2y
        for other_obj in other_objs:
            r = math.dist([self.posx, self.posy],[other_obj.posx, other_obj.posy]) + 15  #distance with a softening factor
            theta = obj.getAngle((other_obj.posy - self.posy),(other_obj.posx - self.posx)) #angle
            m = 50000000000000 #mass of object
            
            if r != 0:
                self.d2x += ((m * scipy.constants.G)/(r**2)) * numpy.cos(theta) #acceleration, velocity, position
                self.d2y += ((m * scipy.constants.G)/(r**2)) * numpy.sin(theta)
                # 
                    
     
    def updateObjVP(self): 
        """
        calculate and update the velocity (dx,dy) and position (posx, posy) of an obj instance
 
        Parameters
        ----------
        self: an instance of obj
 
        Returns
        -------
        void
        """
        dt = 0.1
        
        self.dx += self.d2x * dt
        self.dy += self.d2y * dt
        self.posx += self.dx * dt
        self.posy += self.dy * dt
        self.posx = round(self.posx, 10)
        self.posy = round(self.posy, 10)
        


    def returnobjInfo(self):
      return [self.id, self.posx, self.posy]
    

    #prob works
    #i mean its kinda hard to fuck this up
    @classmethod
    def updateRdf(cls):
        #clear R df
        RcreateDf = robjects.globalenv['createDf']
        RcreateDf()

        #add all exiting objects to df #############
        RappendRow = robjects.globalenv['AppendRow']
        for i in cls.existing_objs:
            RappendRow([i.id, i.posx, i.posy])

    
    # helper function: find the angle in radians between the line from origin to (ydiff,xdiff) and the x axis
    #Parameters: ydiff = y coordinate of object
    #            xdiff = x coordinate
    #returns the angle in radians
    @classmethod
    def getAngle(cls, ydiff, xdiff):
        #edge case: xdiff = 0 
        if xdiff == 0:
            if ydiff > 0 :
                return math.pi/2
            else:
                return -math.pi/2
        #xdiff and ydiff cant both be 0 because updateobjA() ensured that distance is not 0
        
        #edge case: ydiff = 0
        if ydiff == 0:
            if xdiff > 0 :
                return 0
            else:
                return math.pi
            
            
        theta = numpy.arctan(ydiff/xdiff)
        if xdiff < 0:
            theta = math.pi + theta
        return theta

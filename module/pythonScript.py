import rpy2
import math
import numpy
import scipy
from scipy import constants

class agent():
    existing_agents = []

    
    def __init__(self, id, posx, posy, dx, dy, d2x, d2y):
        self.id = id
        self.posx = posx
        self.posy = posy
        self.dx = dx
        self.dy = dy
        self.d2x = d2x
        self.d2y = d2y
        agent.existing_agents.append(self)
        


    def updateAgentA(self): 
        """
        calculate and update the acceleration (d2x,d2y) of an instance
 
        Parameters
        ----------
        self: agent
            an instance of agent
 
        Returns
        -------
        void
        """
        self.d2x = 0
        self.d2y = 0
        
        #get a list of all other agents
        other_agents = list(agent.existing_agents)
        other_agents.remove(self)
        
        #add the acceleration due to gravitation of every other agent to self.d2x/d2y
        for other_agent in other_agents:
            r = math.dist([self.posx, self.posy],[other_agent.posx, other_agent.posy]) + 15  #distance with a softening factor
            theta = agent.getAngle((other_agent.posy - self.posy),(other_agent.posx - self.posx)) #angle
            m = 50000000000000 #mass of object
            
            if r != 0:
                self.d2x += ((m * scipy.constants.G)/(r**2)) * numpy.cos(theta) #acceleration, velocity, position
                self.d2y += ((m * scipy.constants.G)/(r**2)) * numpy.sin(theta)
                    
       
    def updateAgentVP(self): 
        """
        calculate and update the velocity (dx,dy) and position (posx, posy) of an instance
 
        Parameters
        ----------
        self: agent
            an instance of agent
 
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


    @classmethod
    def getAngle(cls, ydiff, xdiff):
        """
        helper function: find the angle in radians between the line from origin to (ydiff,xdiff) and the x axis
 
        Parameters
        ----------
        ydiff: int, float
            y coordinate
        xdiff: int, float
            x coordinate
 
        Returns
        -------
        float
            the angle in radians
        """
        #edge case: xdiff = 0 
        if xdiff == 0:
            if ydiff > 0 :
                return math.pi/2
            else:
                return -math.pi/2
        #xdiff and ydiff cant both be 0 because updateAgentA() ensured that distance is not 0
        
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
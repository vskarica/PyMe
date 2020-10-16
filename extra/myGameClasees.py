from math import *
class v2d:  #https://www.python-course.eu/python3_magic_methods.php
    def __init__(self,xy=(0,0)):
        #if isinstance(o, tuple):
        #if type(test_tup) is tuple:
        self.xy=xy

    def __add__(self, other):
        return v2d((self.xy[0]+other.xy[0],self.xy[1]+other.xy[1]))
    
    def __sub__(self, other):
        return v2d((self.xy[0]-other.xy[0],self.xy[1]-other.xy[1]))
    
    def __mul__(self,factor):
        return v2d((self.xy[0]*factor,self.xy[1]*factor))

    def __str__(self):
        return str(self.xy)+", "+str(self.len())

    def len(self):
        return sqrt(self.xy[0]**2+self.xy[1]**2)

    def unitV(self):
        d=self.len()
        return v2d(
                (
                    self.xy[0]/d,
                    self.xy[1]/d
                )
            )
    
    def distance(self,other):
        return sqrt(
                (
                    max(self.xy[0],other.xy[0])
                    -min(self.xy[0],other.xy[0])
                )**2+
                (
                    max(self.xy[1],other.xy[1])
                    -min(self.xy[1],other.xy[1])
                )**2
            )
    
    def rotate(self,angle):
        return (
                round(self.xy[0]*cos(angle)-self.xy[1]*sin(angle),5),
                round(self.xy[0]*sin(angle)+self.xy[1]*cos(angle),5)
            )
    

class GameObject: 
    def __init__ (self,xy=(0,0),w=0,h=0):
        self.xy=xy
        self.w=w
        self.h=h
    
    def gsxy(self,xy=None):
        if xy==None: return self.xy
        else: self.xy=xy

    def rect(self):
        x,y=self.xy
        return (x,y,self.w,self.h)


        
def inicirajGrafiku():
    

class myGameVars:
    def __init__(self):
        self.considerEvent=[
            []
        ]
    
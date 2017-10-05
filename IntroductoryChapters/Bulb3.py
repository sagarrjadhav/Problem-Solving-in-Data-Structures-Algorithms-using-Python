#!/usr/bin/env python
""" Documentation of module Bulb """
class Bulb(object):
    """ Documentation of class Bulb """
    TotalBulbCount = 0          # Class Variables
   
    def __init__(self):         # Constructor
        """ Documentation of method __init__ """
        Bulb.TotalBulbCount += 1
        self.isOn = False       # Instance Variables 

    @classmethod
    def getBulbCount(cls):
        """ Documentation of method getBulbCount """
        return cls.TotalBulbCount
    
    def turnOn(self):           # Instance Method
        """ Documentation of method turnOn """
        self.isOn = True
    
    def turnOff(self):          # Instance Method
        """ Documentation of method turnOff """
        self.isOn = False
    
    def isOnFun(self):          # Instance Method
        """ Documentation of method isOnFun """
        return self.isOn


class AdvanceBulb(Bulb):
    """ Documentation of class AdvanceBulb """   
    def __init__(self):                 # Constructor
        """ Documentation of method __init__ """
        self.intensity = 0 # Instance Variables 
        Bulb.__init__(self)
   
    def setIntersity(self, i):          # Instance Method
        """ Documentation of method setIntersity """
        self.intensity = i
              
    def getIntersity(self, i):          # Instance Method
        """ Documentation of method setIntersity """
        return self.intensity


""" Documentation of module BulbDemo """
class BulbDemo(object):
    """ Documentation of class BulbDemo """
    @classmethod
    def main(cls, args):
        """ Documentation of method main """
        # b = Bulb()
        c = AdvanceBulb()
        print Bulb.getBulbCount()
        print c.isOnFun()

if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)
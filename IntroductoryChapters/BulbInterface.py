#!/usr/bin/env python
from abc import ABCMeta
from abc import abstractmethod

""" Source for module BulbInterface """
class BulbInterface(object):
    """ Source for interface BulbInterface """
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def turnOn(self):
        """ Source for method turnOn """
        pass
    
    @abstractmethod
    def turnOff(self):
        """ Source for method turnOff """
        pass

    @abstractmethod
    def isOnFun(self):
        """ Source for method isOnFun """
        pass

# implements BulbInterface
class Bulb(BulbInterface):
    """ Source for class Bulb """
    class BulbSize:
        """ Source for enum BulbSize """
        SMALL = u'SMALL'
        MEDIUM = u'MEDIUM'
        LARGE = u'LARGE'

    # Class Variables 
    TotalBulbCount = 0

    # Constructor
    def __init__(self):
        """ Source for method __init__ """
        Bulb.TotalBulbCount += 1
        self.isOn = False  # Instance Variables
        self.size = Bulb.BulbSize.MEDIUM

    # Class Method
    @classmethod
    def getBulbCount(cls):
        """ Source for method getBulbCount """
        return cls.TotalBulbCount

    # Instance Method
    def turnOn(self):
        """ Source for method turnOn """
        self.isOn = True

    # Instance Method
    def turnOff(self):
        """ Source for method turnOff """
        self.isOn = False

    # Instance Method
    def isOnFun(self):
        """ Source for method isOnFun """
        return self.isOn

    def getBulbSize(self):
        return self.size

class AdvanceBulb(Bulb):
    """ Source for class AdvanceBulb """
    # Constructor
    def __init__(self):
        """ Source for method __init__ """
        self.intensity = 0 # Instance Variables 
        Bulb.__init__(self)
        
    # Instance Method
    def setIntersity(self, i):
        """ Source for method setIntersity """
        self.intensity = i
        
        # Instance Method
    def getIntersity(self, i):
        """ Source for method setIntersity """
        return self.intensity

""" Source for module BulbDemo """
class BulbDemo(object):
    """ Source for class BulbDemo """
    @classmethod
    def main(cls, args):
        """ Source for method main """
        b = Bulb()
        print "Bulb Size : " + b.getBulbSize()
        print "bulb is on return : " , b.isOnFun()
        b.turnOn()
        print "bulb is on return : " , b.isOnFun()


if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)


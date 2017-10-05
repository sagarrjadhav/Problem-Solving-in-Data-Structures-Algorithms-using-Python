#!/usr/bin/env python
class Bulb(object):
    """ Source for class Bulb """

    # Class Variables 
    TotalBulbCount = 0
    
    # Constructor
    def __init__(self):
        """ Source for method __init__ """
        Bulb.TotalBulbCount += 1
        self.isOn = False  # Instance Variable

    # Class Method
    @classmethod
    def getBulbCount(cls):
        """ Source for method getBulbCount """
        return Bulb.TotalBulbCount

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

""" Source for module BulbDemo """
class BulbDemo(object):
    """ Source for class BulbDemo """
    @classmethod
    def main(cls, args):
        """ Source for method main """
        b = Bulb()
        print "bulb is on return : " , b.isOnFun()
        b.turnOn()
        print "bulb is on return : " , b.isOnFun()
        print Bulb.getBulbCount()


if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)
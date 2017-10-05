#!/usr/bin/env python

class Bulb(object):
    """ Source for class Bulb """
    class BulbSize:
        """ Source for enum BulbSize """
        SMALL = u'SMALL'
        MEDIUM = u'MEDIUM'
        LARGE = u'LARGE'

    # Constructor
    def __init__(self):
        """ Source for method __init__ """
        self.isOn = False  # Instance Variables
        self.size = Bulb.BulbSize.MEDIUM

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
    
    def setBulbSize(self, value):
        self.size = value

class BulbDemo(object):
    """ Source for class BulbDemo """
    @classmethod
    def main(cls, args):
        """ Source for method main """
        b = Bulb()
        print "Bulb Size : " + b.getBulbSize()

if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)
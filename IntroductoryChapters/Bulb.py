#!/usr/bin/env python

class Bulb(object):
    """ Source for class Bulb """
    def __init__(self):         # Constructor
        """ Source for method __init__ """
        self.isOn = False       # Instance Variable
    
    def turnOn(self):           # Instance Method
        """ generated source for method turnOn """
        self.isOn = True
    
    def turnOff(self):          # Instance Method
        """ generated source for method turnOff """
        self.isOn = False
    
    def isOnFun(self):          # Instance Method
        """ generated source for method isOnFun """
        return self.isOn

""" generated source for module BulbDemo """
class BulbDemo(object):
    """ generated source for class BulbDemo """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        b = Bulb()
        print "bulb is on return : " , b.isOnFun()
        b.turnOn()
        print "bulb is on return : " , b.isOnFun()
        
        c = Bulb()
        print "bulb c is on return : " , c.isOnFun()


if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)
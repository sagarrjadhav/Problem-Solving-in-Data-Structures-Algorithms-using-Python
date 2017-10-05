#!/usr/bin/env python
""" Source for module Introduction """
class IncrementDemo(object):
    """ Source for class Introduction """
    @classmethod
    def increment2(cls, var):
        """ Source for method increment """
        var += 1

    @classmethod
    def main2(cls, args):
        """ Source for method main """
        var = 1
        print "Value before increment :" , var
        cls.increment(var)
        print "Value after increment :" , var
        
    class MyInt(object):
        """ Source for class MyInt """
        value = 0

    @classmethod
    def increment(cls, value):
        """ Source for method increment """
        value.value += 1   
        
    @classmethod
    def main(cls, args):
        """ Source for method main """
        var = cls.MyInt()
        print "Value before increment :" , var.value
        cls.increment(var)
        print "Value after increment :" , var.value  
        

if __name__ == '__main__':
    import sys
    IncrementDemo.main(sys.argv)
#!/usr/bin/env python
class VariableType(object):
    @classmethod
    def main(cls, args):
        maxInt = sys.maxint
        longstart = maxInt + 1
        minInt = -1 * (maxInt+1)
        floatvalue = 0.1
        str = "hello, world!"
        print "type of maxint" , type(maxInt) , "value : " , maxInt
        print "type of minInt" , type(minInt) , "value : " , minInt
        print "type of longstart" , type(longstart) , "value : " , longstart
        print "type of floatvalue" , type(floatvalue) , "value : " , floatvalue 
        print "type of str" , type(str) , "value : " , str             


if __name__ == '__main__':
    import sys
    VariableType.main(sys.argv)
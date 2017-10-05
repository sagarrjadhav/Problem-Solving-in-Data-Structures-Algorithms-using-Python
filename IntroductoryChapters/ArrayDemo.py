#!/usr/bin/env python
""" generated source for module ArrayDemo """
class ArrayDemo(object):
    """ generated source for class ArrayDemo """
    def __init__(self):
        """ generated source for method __init__ """
        self.numbers = [0] * 100

    def addValue(self, index, data):
        """ generated source for method addValue """
        self.numbers[index] = data

    def getValue(self, index):
        """ generated source for method getValue """
        return self.numbers[index]



""" generated source for module Main """
class Main(object):
    """ generated source for class Main """
    def __init__(self):
        """ generated source for method __init__ """
        #  TODO Auto-generated constructor stub

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  TODO Auto-generated method stub
        d = ArrayDemo()
        d.addValue(0, 1)
        d.addValue(1, 2)
        print d.getValue(0)
        print d.getValue(1)


if __name__ == '__main__':
    import sys
    Main.main(sys.argv)

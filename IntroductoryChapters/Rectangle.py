#!/usr/bin/env python
from Shape import Shape
""" generated source for module Rectangle """
class Rectangle(Shape):
    """ generated source for class Rectangle """
    def __init__(self, w=1, l=1):
        """ generated source for method __init__ """
        self.width = w
        self.length = l

    def setWidth(self, w):
        """ generated source for method setWidth """
        self.width = w

    def setLength(self, l):
        """ generated source for method setLength """
        self.length = l

    def area(self):
        """ generated source for method area """ 
        return self.width * self.length  #  Area = width * length

    def perimeter(self):
        """ generated source for method perimeter """
        return 2 * (self.width + self.length)  #  Perimeter = 2(width + length)


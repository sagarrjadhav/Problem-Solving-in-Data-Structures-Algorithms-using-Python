#!/usr/bin/env python
from Circle import Circle
from Rectangle import Rectangle

class ShapeDemo(object):
    @classmethod
    def main(cls, args):
        width = 2
        length = 3
        rectangle = Rectangle(width, length)
        print "Rectangle width:" , width , "and length:" , length , "Area:" , rectangle.area() , "Perimeter:" , rectangle.perimeter()
        radius = 10
        circle = Circle(radius)
        print "Circle radius:" , radius, "Area:" , circle.area(), "Perimeter:" , circle.perimeter()


if __name__ == '__main__':
    import sys
    ShapeDemo.main(sys.argv)

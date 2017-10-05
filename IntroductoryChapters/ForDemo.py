#!/usr/bin/env python
""" generated source for module ForDemo """
class ForDemo(object):
    """ generated source for class ForDemo """
    text = "Hello, World!"
    PI = 3.141592653589793

    @classmethod
    def main1(cls):
        """ generated source for method main1 """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        totalsum = 0
        for n in numbers:
            totalsum += n
        print "Sum is :: " , totalsum

    @classmethod
    def main2(cls):
        """ generated source for method main2 """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        totalsum = 0
        i = 0
        while i < len(numbers):
            totalsum += numbers[i]
            i += 1
        print "Sum is :: " , totalsum

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        totalsum = 0
        i = 0
        while True:
            totalsum += numbers[i]
            i += 1
            if i >= len(numbers):
                break
        print "Sum is :: " , totalsum


if __name__ == '__main__':
    import sys
    ForDemo.main(sys.argv)

#!/usr/bin/env python
class TypeDemo(object):

    @classmethod
    def main(cls, args):
            value1 = sys.maxint
            value2 = value1 + 1
            value3 = 13.05
            value4 = 3.14j
            value5 = "hello, world!"
            print type(value1),value2, type(value2), type(value3), type(value4),type(value5), value5

if __name__ == '__main__':
    import sys
    TypeDemo.main(sys.argv)



class ParameterPass:
    def __init__(self):
        A = 1
        self.Change(A)
        print A

    def Change(self, B):
        B = 2

class ParameterPass2:
    def __init__(self):
        A = [1]
        self.Change(A)
        print A

    def Change(self, B):
        B.append(2)

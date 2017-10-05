#!/usr/bin/env python
""" source for module HelloWorld """
class HelloWorld(object):
    """ source for class HelloWorld """

    @classmethod
    def main(cls, args):
        """ source for method main """
        print "Hello, World!"

if __name__ == '__main__':
    import sys
    HelloWorld.main(sys.argv)
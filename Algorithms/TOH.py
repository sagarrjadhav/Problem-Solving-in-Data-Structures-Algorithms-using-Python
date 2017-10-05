#!/usr/bin/env python
""" generated source for module TOH """

class TOH(object):
    """ generated source for class TOH """
    
    @classmethod
    def main(cls, args):
        """ generated source for method main """

        cls.TowersOfHanoi(3)

    @classmethod
    def TOHUtil(cls, num, source, dest, temp):
        """ generated source for method TOHUtil """
        if num < 1:
            return
        cls.TOHUtil(num - 1, source, temp, dest)
        print("Move disk" , num , "from peg" , source , "to peg" , dest)
        cls.TOHUtil(num - 1, temp, dest, source)

    @classmethod
    def TowersOfHanoi(cls, num):
        """ generated source for method TowersOfHanoi """
        print("The sequence of moves involved in the Tower of Hanoi are :")
        cls.TOHUtil(num, 'A', 'C', 'B')


if __name__ == '__main__':
    import sys
    TOH.main(sys.argv)

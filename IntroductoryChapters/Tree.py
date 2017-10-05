#!/usr/bin/env python
""" Documentation of module Tree """
class Tree(object):
    """ Documentation of class Tree """
    class Node(object):
        """ Documentation of class Node """
        def __init__(self, v, l=None, r=None):
            """ Documentation of method __init__ """
            self.value = v
            self.lChild = l
            self.rChild = r       
        #  Nested Class Node other fields and methods.    

    def __init__(self):
        """ Documentation of method __init__ """
        self.root = None
    #  Outer Class Tree other fields and methods.
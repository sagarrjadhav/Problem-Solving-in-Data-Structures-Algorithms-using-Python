#!/usr/bin/env python
""" Documentation of module LinkedList """
class LinkedList(object):
    """ Documentation of class LinkedList """
    class Node(object):
        """ Documentation of class Node """
        def __init__(self, v, n=None):
            """ Documentation of for method __init__ """
            self.value = v
            self.next = n


    def __init__(self):
        """ Documentation of  method __init__ """
        self.head = None
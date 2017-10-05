#!/usr/bin/env python
""" generated source for module Calculator """
class Calculator(object):
    """ generated source for class Calculator """
    def __init__(self, value=0):
        """ generated source for method __init__ """
        self.value = value

    def reset(self):
        """ generated source for method reset """
        self.value = 0

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def add(self, data):
        """ generated source for method add """
        self.value = self.value + data

    def increment(self):
        """ generated source for method increment """
        self.value += 1

    def subtract(self, data):
        """ generated source for method subtract """
        self.value = self.value - data

    def decrement(self):
        """ generated source for method decrement """
        self.value -= 1
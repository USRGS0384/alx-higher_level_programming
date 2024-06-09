#!/usr/bin/python3
'''Module for Base class.'''

class Base

''' This is a representation of the base of OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            seld.id = Base.__nb_objects


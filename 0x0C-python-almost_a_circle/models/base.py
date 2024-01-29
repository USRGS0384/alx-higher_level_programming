#!/usr/bin/python3
'''module for Base class.'''

Class base:

    def__init__(self, id=None)
''' A representation of the base of the oop hierarchy.'''

    __nb-objects = 0

    def__init__(self, id=None):
        '''constructor.'''

        if id is non None:
            seld.id = id

        else:
            Bases.__nb-objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/env python

class Tag:

    def __init__(self, i):
        """initialise an RFID tag with the given ID a blank memory and an active
        boolean set to False"""
        self.id = i
        self.memory = []
        self.active = False

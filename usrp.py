#!/usr/bin/env python
from emitter import Emitter
from receiver import Receiver
from computer import Computer

class USRP:
    def __init__(self, f):
        """initialise an USRP with the emitter part and the receiver part
        to the given frequency"""
        self.emitter = Emitter(f)
        self.receiver = Receiver(f)

    def setComputer(self, c):
        self.computer = c

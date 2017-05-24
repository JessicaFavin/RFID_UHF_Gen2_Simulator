#!/usr/bin/env python
from usrp import USRP
from computer import Computer

if __name__ == '__main__':
    print "This is a RFID communication simulator"
    print "Welcome !"

    usrp = USRP(915) #sets USRP to 915 MHz
    computer = Computer(usrp) #sets computer with usrp
    usrp.setComputer(computer) #sets usrp with computer

#!/usr/bin/env python
from usrp import USRP
from computer import Computer
from tag import Tag
import logging

if __name__ == '__main__':
    print ("This is a RFID communication simulator")
    print ("Welcome !")
    logger = logging.getLogger(__name__)

    usrp = USRP(915) #sets USRP to 915 MHz
    computer = Computer(usrp) #sets computer with usrp
    usrp.setComputer(computer) #sets usrp with computer

    logger.info("Generation des tags...")
    tags = []
    for i in range(1,11):
    	tags.append(Tag())
    logger.info("10 tags générés")

    usrp.setTags(tags)
    logger.info("Tags set in URSP")

    computer.start()
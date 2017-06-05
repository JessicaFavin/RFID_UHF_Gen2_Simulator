#!/usr/bin/env python
from emitter import Emitter
from receiver import Receiver
from computer import Computer
import logging

class USRP:
	def __init__(self, f):
		self.logger = logging.getLogger(__name__)
		logging.basicConfig(level=logging.DEBUG)
		self.emitter = Emitter(f)
		self.logger.info("Emitter is set")
		self.receiver = Receiver(f)
		self.logger.info("Receiver is set")

	def setComputer(self, c):
		self.computer = c
		self.logger.info("Computer is set")

	def send(self, msg):
		self.logger.info("Look for tags begining with : "+ msg)
		response = self.emitter.sendMessage(msg)
		return self.receiver.receiveMessage(response)

	def setTags(self, tags):
		self.emitter.setTags(tags)
		self.logger.info("Tags set in emitter")

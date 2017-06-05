#!/usr/bin/env python
import logging
from collision_management import Collision_management

class Receiver:
	def __init__(self, f):
		self.logger = logging.getLogger(__name__)
		self.frequency = f
		self.collision = Collision_management()
		pass

	'''retrourne une autre liste'''
	def receiveMessage(self, tags):
		return self.collision.scramble_tags(tags) 
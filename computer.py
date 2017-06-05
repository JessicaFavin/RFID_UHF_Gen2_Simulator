#!/usr/bin/env python
#from usrp import USRP
import logging
import uuid
import hashlib

class Computer:
	def __init__(self, u):
		self.logger = logging.getLogger(__name__)
		self.usrp = u
		self.identifiedTags = []

	def sendMsg(self,msg):
		self.usrp.send(msg)

	def testCollision(self, tags):
		for tag in tags:
			if tag.hash != hashlib.md5((tag.id).encode()).hexdigest():

				return True
		return False

	def identifyTagsBeginningWith(self, str):
		response = self.usrp.send(str)
		print("beg: "+str)
		if self.testCollision(response):
			print("MAGIC")
			self.identifyTagsBeginningWith(str+'0')
			self.identifyTagsBeginningWith(str+'1')
		else:
			if response is not None:
				for tag in response:
					self.identifiedTags.append(tag)
					'''self.logger.info("TAG IDENTIFIED: "+ tag.id)'''


	def start(self):
		self.logger.info("Computer start working with usrp and identify the tags")
		self.identifyTagsBeginningWith("0")
		self.identifyTagsBeginningWith("1")
		self.logger.info(str(len(self.identifiedTags))+ " tags identified by the computer")
		i = 0
		print("-----IDENTIFIED-----")
		for tag in self.identifiedTags:
			self.logger.debug("TAG "+ str(i)+" : 	id :"+ tag.id)
			i+=1
		i = 0
		print("-------REAL------")
		for tag in self.usrp.emitter.tags:
			self.logger.debug("TAG "+ str(i)+" : 	id :"+ tag.id)
			i+=1
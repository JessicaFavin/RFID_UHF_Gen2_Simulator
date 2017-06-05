#!/usr/bin/env python
import logging
import uuid
import hashlib

class Tag:

	def hexStringToByteArray(self, hex):
		hex = hex.replace("-","")
		result =[]
		for i in range (0, len(hex)-1, 2):
			hexVal = hex[i:i+2]
			intVal = int(hexVal, 16)
			binVal = bin(intVal)[2:].zfill(8)
			result.append(binVal)
		return result

	def __init__(self, id=None, hash=None):
		self.logger = logging.getLogger(__name__)
		"""initialise an RFID tag with the given ID a blank memory and an activ boolean set to False"""
		if id is None:
			self.id = uuid.uuid4().hex
		else:
			self.id = id
		if hash is None:
			self.hash = hashlib.md5((self.id).encode()).hexdigest()
		else:
			self.hash = hash
		self.memory = []
		self.active = False
		self.logger.debug('New Tag : id: '+ str(self.id)+' hash: ['+ str(self.hash) + '] active: '+ str(self.active))
		'''self.logger.debug(''.join(self.hexStringToByteArray(self.id)))'''


	def respond(self, begin):
		if ''.join(self.hexStringToByteArray(self.id)).startswith(begin):
			'''self.logger.debug('begin: '+begin+ ' id: '+''.join(self.hexStringToByteArray(self.id)))'''
			return self
		else:
			return None

    
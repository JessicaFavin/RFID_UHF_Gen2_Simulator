#!/usr/bin/env python
import logging
class Emitter:
	def __init__(self, f):
		self.logger = logging.getLogger(__name__)
		self.frequency = f
		pass

	def sendMessage(self, msg):
		response = []
		for tag in self.tags:
			if tag.respond(msg) is not None:
				response.append(tag)
		return response

	def setTags(self, tags):
		self.tags = tags
		'''for tag in tags:
			self.logger.info("tag : "+ tag.id)'''
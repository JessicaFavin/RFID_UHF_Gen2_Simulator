#!/usr/bin/env python
import random
from tag import Tag

class Collision_management:

	def scramble_tags(self, tags):
		result = []
		if len(tags) is not 1:
			for tag in tags:
				'''print('avant: '+tag.id)'''
				result.append(Tag(''.join(random.sample(tag.id, len(tag.id))), tag.hash))
				'''print('après: '+tag.id)'''
		else:
			result.append(Tag(tags[0].id, tags[0].hash))
		return result

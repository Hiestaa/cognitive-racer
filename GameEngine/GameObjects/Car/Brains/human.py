# -*- coding: utf8 -*-

import logging
import pygame

from Graphx import graphx
from conf import conf
from EventsManager import eventsManager


class HumanBrain(object):
	"""
	The brain of the car that is controlled by the human
	"""
	def __init__(self, model):
		"""
		Initialize the brain and register the key events
		"""
		super(HumanBrain, self).__init__()
		self._model = model
		self._nextDecision = 'halt'

		# register events
		eventsManager.registerEvent(
			"%s.accelerate" % self._model.objectName,
			(pygame.KEYDOWN, pygame.K_UP),
			self.onKeyUp)
		eventsManager.registerEvent(
			"%s.decelerate" % self._model.objectName,
			(pygame.KEYDOWN, pygame.K_DOWN),
			self.onKeyDown)
		eventsManager.registerEvent(
			"%s.turnRight" % self._model.objectName,
			(pygame.KEYDOWN, pygame.K_RIGHT),
			self.onKeyRight)
		eventsManager.registerEvent(
			"%s.turnLeft" % self._model.objectName,
			(pygame.KEYDOWN, pygame.K_LEFT),
			self.onKeyLeft)

	def onKeyUp(self):
		self._nextDecision = 'accelerate'

	def onKeyDown(self):
		self._nextDecision = 'break'

	def onKeyRight(self):
		self._nextDecision = 'turnRight'

	def onKeyLeft(self):
		self._nextDecision = 'turnLeft'

	def decision(self):
		"""
		Take the decision about what to do next.
		"""
		decision, self._nextDecision = self._nextDecision, 'halt'
		logging.info("Car %s will decide to %s"
					  % (self._model.objectName, decision))
		return decision

		
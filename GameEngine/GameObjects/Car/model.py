# -*- coding: utf8 -*-

import logging
import pygame
import json
import os 
import math

from conf import conf
from GameEngine.GameObjects.gameObjectModel import GameObjectModel
from state import CarState


class CarModel(GameObjectModel):
	"""
	Represent the data stored by a car, such as his position, heading,
	history and desision parameter. 
    """
	def __init__(self, initHeading=(1, 0), constants=None, **kwargs):
		"""
		Inintialize a new car model
		initHeading -- initial heading of the car
		constants -- dict containing constant values of the car. The default
					 is the one specified of the conf
		**kwargs -- other argments are given to the GameObjectModel constructor
		"""
		super(CarModel, self).__init__(**kwargs)
		logging.log(1, "Trace: CarModel.__init__(%s, %s, %s)"
						% (initHeading, constants, kwargs))
		logging.info("CarModel initialized at position: %s with heading %s"
					 % (self._position, initHeading))
		self._headingAngle = math.atan2(*initHeading) % (2 * math.pi)
		logging.debug("CarModel init heading angle is: %.5f rad" % self._headingAngle)
		logging.debug("CarModel init heading angle is: %.5f deg" 
					% math.degrees(self._headingAngle))
		self._headingVector = initHeading
		self._rotatedSurface = pygame.transform.rotate(
			self.surface, math.degrees(self._headingAngle))

		self.rect = self._rotatedSurface.get_rect()
		self.rect.center = self.position

		self._velocity = 0.0

		self._constants = constants or \
			conf['game_engine']['car']['default_constants']

	def rotate(self, angle):
		"""
		Rotate the car: if the angle has changed, the rotatedSurface is 
		re-computed using pygame.transform.rotate.
		"""
		logging.debug("Rotate called with angle: %s" % str(angle))
		if angle % (2 * math.pi) == self._headingAngle:
			return;
		self.headingAngle = angle
		self._rotatedSurface = pygame.transform.rotate(
			self.surface, math.degrees(self.headingAngle))
		self.rect = self._rotatedSurface.get_rect()
		self.rect.center = self.position

	@property
	def headingAngle(self):
	    return self._headingAngle
	@headingAngle.setter
	def headingAngle(self, value):
	    self._headingAngle = value % (2 * math.pi)
	    self._headingVector = (
	    	math.sin(self._headingAngle), math.cos(self._headingAngle))

	@property
	def headingVector(self):
	    return self._headingVector
	@headingVector.setter
	def headingVector(self, value):
	    self._headingVector = value
	    self._headingAngle = math.atan2(*value)
	
	@property
	def velocity(self):
	    return self._velocity
	@velocity.setter
	def velocity(self, value):
	    self._velocity = value
	
	def constant(self, name):
		"""
		Return the car constant according to its name:
		Available constant: 
			* maniability
			* max_speed
			* acceleration
			* break
		"""
		return self._constants[name]

	@property
	def rotatedSurface(self):
	    return self._rotatedSurface

	
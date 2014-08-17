# -*- coding: utf8 -*-

import logging
import math

from Graphx import graphx
from GameEngine.GameObjects.gameObjectBehaviour import GameObjectBehaviour
from Brains.human import HumanBrain
from conf import conf

class CarBehaviour(GameObjectBehaviour):
	brainTypes = {
		'human': HumanBrain
	}
	"""
    Behaviour of the car. It handles the car at its current position.
	"""
	def __init__(self, brainType, ruleChecker, model):
		"""
		Initialize a new Behaviour object for the car.
		It needs a brain which will take the actual decisions of the actions,
		and the model that holds the state history
		"""
		super(CarBehaviour, self).__init__(model)
		self._brain = CarBehaviour.brainTypes[brainType](model)
		self._ruleChecker = ruleChecker
		self._newVelocity = None
		self._newPosition = None
		self._newHeading = None
		self._actions = {
			'accelerate': self.accelerate,
			'break': self.breaks,
			'turnRight': self.turnRight,
			'turnLeft': self.turnLeft,
			'halt': self.halt
		}
	

	def move(self):
		"""
		set the new position of the car using the current velocity and
	 	the current heading
		"""
		self._newPosition = \
			(self._model.position[0] + 
				self._newVelocity * self._model.headingVector[0],
			 self._model.position[1] + 
				self._newVelocity * self._model.headingVector[1])

	def halt(self):
		"""
		If this action is called at this turn, the velocity and the heading
		stay the same
		"""
		self._newVelocity = self._model.velocity
		self._newHeading = self._model.headingAngle
		self.move()

	def accelerate(self):
		"""
		Increase the velocity by the car's acceleration
		If max_speed is reached, the car simply keep its current speed.
		The heading does not change
		"""
		self._newVelocity = \
			self._model.velocity + self._model.constant('acceleration')
		if self._newVelocity > self._model.constant('max_speed'):
			self._newVelocity = self._model.constant('max_speed')
		self._newHeading = self._model.headingAngle
		self.move()

	def breaks(self):
		"""
		Breaks using the car's break constant.
		If the car is already stopped, nothing happen.
		The heading does not change
		"""
		self._newVelocity = \
			self._model.velocity - self._model.constant('break')
		if self._newVelocity < 0:
			self._newVelocity = 0
		self._newHeading = self._model.headingAngle
		self.move()

	def turnRight(self):
		"""
		Turn right relatively to the car's heading using the car's maniability.
		The velocity does not change
		"""
		self._newHeading = self._model.headingAngle - \
			self._model.constant('maniability')
		self._newVelocity = self._model.velocity
		self.move()

	def turnLeft(self):
		"""
		Turn left relatively to the car's heading using the car's maniability
		The velocity does not change
		"""
		self._newHeading = self._model.headingAngle + \
			self._model.constant('maniability')
		self._newVelocity = self._model.velocity
		self.move()

	def update(self, stateManager):
		"""
		Use the brain the take the decision about what is the next action, then
		update the model according to what has been decided.
		"""
		decision = self._brain.decision()
		self._actions[decision]()
		self._model.rotate(self._newHeading)
		self._model.velocity = self._newVelocity
		self._model.position = self._newPosition
#		self._ruleChecker.check(self._model.getCurrentState(),
#								self._model.getPreviousState())



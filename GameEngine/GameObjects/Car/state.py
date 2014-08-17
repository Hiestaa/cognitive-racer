# -*- coding: utf8 -*-

import logging

from conf import conf


class CarState (object):
	"""
	Represent the state of the car at a fixed point of the time
	"""

	def __init__(self, position, heading, velocity):
		super(CarState, self).__init__()
		logging.log(1, "Trace: CarState.__init__(%s, %s)" % (position, heading))
		self._position = position
		self._heading = heading  # heading is a unit vector
		self._velocity = velocity

	@property
	def heading(self):
	    return self._heading
	@heading.setter
	def heading(self, value):
	    self._heading = value


	@property
	def position(self):
	    return self._position
	@position.setter
	def position(self, value):
	    self._position = value
	
	@property
	def velocity(self):
	    return self._velocity
	@velocity.setter
	def velocity(self, value):
	    self._velocity = value
	
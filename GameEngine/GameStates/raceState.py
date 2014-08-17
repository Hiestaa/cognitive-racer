# -*- coding: utf8 -*-

import logging
from pprint import pformat

from state import State
from GameEngine.GameObjects.map import Map

class RaceState(State):
	"""Represent the state of the game during the race"""
 	_instance = None

	def __init__(self):
		"""
		Create a new race state
		"""
		super(State, self).__init__()
		self._map = Map()

	def update(self, stateManager):
		self._map.update(stateManager)

	def render(self, interpolation):
		self._map.render(interpolation)

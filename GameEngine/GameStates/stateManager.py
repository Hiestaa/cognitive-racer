# -*- coding: utf8 -*-

import logging

from conf import conf
from raceState import RaceState


class StateManager(object):
	"""Manage the state stack of the game"""
	def __init__(self):
		super(StateManager, self).__init__()
		logging.log(1, "Trace: StateManager.__init__()")
		self._state_stack = []
		# when initalizing, the introstate is the first to be
		# pushed on the stack
		self.pushState(RaceState.getInstance())

	def update(self):
		for state in self._state_stack:
			state.update(self)

	def render(self, interpolation):
		for state in self._state_stack:
			state.render(interpolation)

	def popState(self):
		self._state_stack.pop()

	def pushState(self, state):
		self._state_stack.append(state)

	def changeState(self, state):
		self.popState()
		self.pushState(state)

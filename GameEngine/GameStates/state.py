# -*- coding: utf8 -*-

import logging
from pprint import pformat


class State(object):
	"""Represent a base state of the game"""
 	_instance = None

	@classmethod
	def createInstance(cls, **kwargs):
		logging.debug("State: %s.createInstance(%s)" % (cls, pformat(kwargs)))
		if cls._instance is not None and isinstance(cls._instance, cls):
			logging.warning("Overriding existing instance of %s" % cls)
		cls._instance = cls(**kwargs)			

	@classmethod
	def getInstance(cls):
		if cls._instance is None or not isinstance(cls._instance, cls):
			cls._instance = cls()
		return cls._instance

	def __init__(self):
		super(State, self).__init__()

	def update(self, stateManager):
		pass

	def changeState(self, stateManager, state):
		stateManager.changeState(state)

	def pushState(self, stateManager, state):
		stateManager.pushState(state)

	def popState(self, stateManager):
		stateManager.popState()

	def render(self, interpolation):
		pass

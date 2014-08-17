# -*- coding: utf8 -*-

import logging

import pygame


class GameObjectBehaviour(object):
	"""
        Handle the behaviour of a default game object
	"""
	def __init__(self, model):
		"""
		Initialize the behaviour of the game object
		model -- the model of the game object
		"""
		super(GameObjectBehaviour, self).__init__()
		logging.log(1, "Trace: GameObjectBehaviour.__init__(%s)" % model)
		self._model = model

	def update(self, stateManager):
		pass

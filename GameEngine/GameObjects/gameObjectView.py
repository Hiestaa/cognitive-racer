# -*- coding: utf8 -*-

import logging

from Graphx import graphx


class GameObjectView(object):
	"""
    View of the game object. It handles the drawing of a game object
	"""
	def __init__(self, model):
		super(GameObjectView, self).__init__()
		self._model = model


	def render(self, interpolation):
		graphx.draw(self._model.surface, self._model.rect)




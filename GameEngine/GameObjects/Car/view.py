# -*- coding: utf8 -*-

import logging

import pygame

from Graphx import graphx
from GameEngine.GameObjects.gameObjectView import GameObjectView
from conf import conf

class CarView(GameObjectView):
	"""
    View of the car. It handles the car at its current position.
	"""

	def render(self, interpolation):
		logging.debug("Drawing %s at position %s" % (self._model.objectName, self._model.position) )
		graphx.draw(self._model.rotatedSurface, self._model.rect)

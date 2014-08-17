# -*- coding: utf8 -*-

import logging

from Graphx import graphx
from GameEngine.GameObjects.gameObjectBehaviour import GameObjectBehaviour
from conf import conf

class MapBehaviour(GameObjectBehaviour):
	"""
    Behaviour of the map. It mostly handles the updating of the cars racing 
    on the map.
	"""
	def update(self, stateManager):
		for car in self._model.cars:
			car.update(stateManager)


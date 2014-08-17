# -*- coding: utf8 -*-

import logging

from Graphx import graphx
from gameObjectView import GameObjectView
from conf import conf

class MapView(GameObjectView):
	"""
    View of the map. It handles the drawing of the tiles of the map.
	"""

	def render(self, interpolation):
		super(MapView, self).render(interpolation)
		for x in xrange(self._model.size[0]):
			for y in xrange(self._model.size[1]):
				graphx.draw(self._model.getTile((x, y)),
							(x * conf['resources']['game']['tile_size'],
							 y * conf['resources']['game']['tile_size']))
		for car in self._model.cars:
			car.render(interpolation)


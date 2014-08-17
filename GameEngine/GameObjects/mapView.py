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
		if self._model.mapSurface is None:
			self._model.initMapSurface()
			for x in xrange(self._model.size[0]):
				for y in xrange(self._model.size[1]):
					graphx.draw(self._model.getTile((x, y)),
								(x * conf['resources']['game']['tile_size'],
								 y * conf['resources']['game']['tile_size']),
								destination=self._model.mapSurface)
		graphx.draw(self._model.mapSurface)
		for car in self._model.cars:
			car.render(interpolation)


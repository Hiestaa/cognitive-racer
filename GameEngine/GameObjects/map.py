# -*- coding: utf8 -*-

import logging
from mapBehaviour import MapBehaviour
from mapView import MapView
from mapModel import MapModel
from gameObject import GameObject
from conf import conf


class Map(GameObject):
	"""
	Represent the map of the race
	"""
	def __init__(self, **kwargs):
		"""
		Initialize the game object
		kwargs -- the keywords arguments are given to the mapModel
		"""
		model = MapModel(**kwargs)
		view = MapView(model)
		behaviour = MapBehaviour(model)
		super(Map, self).__init__(
			gameObjectModel=model, gameObjectBehaviour=behaviour,
			gameObjectView=view)


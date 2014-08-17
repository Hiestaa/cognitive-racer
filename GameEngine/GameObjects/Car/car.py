# -*- coding: utf8 -*-

import logging

from behaviour import CarBehaviour
from view import CarView
from model import CarModel
from GameEngine.GameObjects.gameObject import GameObject
from conf import conf


class Car(GameObject):
	"""
	Represent the map of the race
	"""
	def __init__(self, **kwargs):
		"""
		Initialize the game object
		kwargs -- the keywords arguments are given to the carModel
		"""
		model = CarModel(**kwargs)
		view = CarView(model)
		behaviour = CarBehaviour('human', None, model)
		super(Car, self).__init__(
			gameObjectModel=model, gameObjectBehaviour=behaviour,
			gameObjectView=view)
		logging.log(1, "Trace: Car.__init__(%s)" % kwargs)


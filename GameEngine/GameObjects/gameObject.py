# -*- coding: utf8 -*-

import logging
from gameObjectBehaviour import GameObjectBehaviour
from gameObjectView import GameObjectView
from gameObjectModel import GameObjectModel
from conf import conf


class GameObject(object):
	"""
	Represent any GameObject of the game. 
	A game object uses a behaviour to update its internal data, a model to
	store its internal data and a view to display it.
	"""
	def __init__(self, gameObjectModel=None, gameObjectBehaviour=None, 
				gameObjectView=None, **kwargs):
		"""
		Initialize the game object
		gameObjectModel -- a custom model for this game object. Note that if
						 this parameter is provided, all the other (except
						 gameObjectBehaviour and gameObjectView) will be ignored
		gameObjectBehaviour -- a custom behaviour for this game object
		gameObjectView -- a custom view for this game object
		kwargs -- the keywords arguments are given to the gameObjectModel
		"""
		super(GameObject, self).__init__()
		logging.log(1, "Trace: GameObject.__init__(%s)"
						% (kwargs))
		if gameObjectModel is None:
			self._model = GameObjectModel(**kwargs)
		else:
			self._model = gameObjectModel

		if gameObjectBehaviour is None:
			self._behaviour = GameObjectBehaviour(self._model)
		else:
			self._behaviour = gameObjectBehaviour

		if gameObjectView is None:
			self._view = GameObjectView(self._model)
		else:
			self._view = gameObjectView

	def update(self, stateManager):
		"""
		Let the behaviour of the game object update the item
		"""
		self._behaviour.update(stateManager)

	def render(self, interpolation):
		"""
		Let the view of the game object render the item
		"""
		self._view.render(interpolation)

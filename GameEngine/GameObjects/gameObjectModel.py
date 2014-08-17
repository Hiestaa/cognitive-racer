# -*- coding: utf8 -*-

import logging
import pygame

from conf import conf


class GameObjectModel(object):
	"""
        Handle the data of a default game object
	"""
	def __init__(self, image=None, initPos=None, 
				 objectName="Unamed"):
		"""
		Initialize the model of the game object
		image -- if string, the link to the image to be used as background for this 
				     game object, otherwise a Surface object is expected
		initPos -- the initial position of the object
		name -- the name of the game object
		"""
		super(GameObjectModel, self).__init__()
		logging.log(1, "Trace: GameObjectModel.__init__(%s, %s, %s)"
						% (image, initPos, objectName))
		# dynamically default the parameters
		if image is None or len(image) == 0:
			image = conf['resources']['game']['default_game_object']
		if initPos is None:
			initPos = (0, 0)

		if type(image) is not list:
			image = [image]

		# load the images
		self._surfaces = []
		for img in image:
			if type(img) is str:
				self._surfaces.append(pygame.image.load(img))
			else:
				self._surfaces.append(img)
		self._currentSurface = 0

		self._position = initPos
		self._objectName = objectName
		self._rect = self._surfaces[0].get_rect()
		self._size = self._rect.size

	@property
	def objectName(self):
	    return self._objectName
	@objectName.setter
	def objectName(self, value):
	    self._objectName = value

	@property
	def position(self):
	    return self._position
	@position.setter
	def position(self, value):
	    self._position = value
	    self._rect.center = value

	@property
	def size(self):
	    return self._size	
	

	def intersect(self, point):
		return self._rect.collidepoint(point)	

	@property
	def rect(self):
	    return self._rect
	@rect.setter
	def rect(self, value):
	    self._rect = value
	

	# returns the current used surface
	@property
	def surface(self):
	    return self._surfaces[self._currentSurface]
	@surface.setter
	def surface(self, value):
	    self._surfaces[self._currentSurface] = value
	    self._rect = self.surface.get_rect()

	# change the current used surface
	def useSurface(self, sid):
		if sid < 0 or sid >= len(self._surfaces):
			logging.warning("Cannot use surface #%d. Only %d surfaces available"
							% (sid, len(self._surfaces)))
			sid = 0
		self._currentSurface = sid

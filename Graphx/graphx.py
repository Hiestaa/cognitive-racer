# -*- coding: utf8 -*-
import pygame
import logging
from functools import wraps

from conf import conf
from videoPlayer import VideoPlayer

# This module intends to provide a proxy to the pygame library,
# also providing a Camera object.

instance = None

def singletonize(method):
	@wraps(method)
	def wrapper(*args, **kwargs):
		return method(instance, *args, **kwargs)
	return wrapper

def init():
	global instance
	instance = Graphx()

class Graphx(object):
	"""Represent the graphx engine"""
	def __init__(self):
		super(Graphx, self).__init__()
		self._screen_size = conf['graphx']['screen_size']
		self._screen = pygame.display.set_mode(self._screen_size)
		self._video_player = VideoPlayer()
		pygame.font.init()

	def playVideo(self, link, on_video_end):
		self._video_player.play(link, on_video_end)

	# Flip the screen and erase the drawing surface.
	# This function should be called once after all the game rendering
	def update(self):
		self._video_player.render()
		pygame.display.flip()
		self._screen.fill(conf['graphx']['screen_base_color'])

	def draw(self, surface, position=(0, 0), clipPos=None, clipSize=None):
		area = None
		if clipPos is not None and clipSize is not None:
			area = pygame.Rect(clipPos, clipSize)
		self._screen.blit(surface, position, area)

	def getScreen(self):
		return self._screen

	def getScreenSize(self):
		return self._screen_size

	def cleanUp(self):
		pygame.font.quit()
		pass

draw = singletonize(Graphx.draw)
update = singletonize(Graphx.update)
playVideo = singletonize(Graphx.playVideo)
getScreen = singletonize(Graphx.getScreen)
getScreenSize = singletonize(Graphx.getScreenSize)
cleanUp = singletonize(Graphx.cleanUp)

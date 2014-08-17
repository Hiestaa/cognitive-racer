# -*- coding: utf8 -*-

import logging
import pygame
import json
import os 

from conf import conf
from tools import square
from gameObjectModel import GameObjectModel
from Car.car import Car


class MapModel(GameObjectModel):
	"""Represent the data stored by the map of the game"""
	GRASS_SYMBOL = 'X'
	TARMAC_SYMBOL = '.'
	LINE_SYMBOL = '-'
	BRAIN_SYMBOLS = {
		'H': 'human'
	}

	def __init__(self, map_file=None, **kwargs):
		super(MapModel, self).__init__(**kwargs)
		if map_file is None:
			map_file = conf['resources']['game']['default_map']
		self._map_file_link = map_file
		self._map_ground = None

		# load map data
		with open(self._map_file_link) as f:
			data = f.read()
			logging.debug("Loaded data: %s" % data)
			self._static_data = json.loads(data)
			logging.info("Loading map: %s - %s"
						 % (self._static_data['name'], 
							self._static_data['description']))
			logging.info("Map made for 1 - %d players"
						 % self._static_data['nb_cars'])
			# load map ground
			with open(os.path.join(os.path.dirname(self._map_file_link), self._static_data['map'])) as f2:
				data = f2.read()
				logging.debug("Loaded data: %s" % data)
				self._map_ground = [[c for c in line] for line in data.split('\n')]

		# load map tiles
		self._tiles = {
			MapModel.TARMAC_SYMBOL: pygame.image.load(
				conf['resources']['game']['tiles']['tarmac']),
			MapModel.GRASS_SYMBOL: pygame.image.load(
				conf['resources']['game']['tiles']['grass']),
			MapModel.LINE_SYMBOL: pygame.image.load(
				conf['resources']['game']['tiles']['line'])	
		}

		# Analyse the map to build efficient structures needed 
		# during the game
		self._cars = []  # list of car objects
		self._line = []  # list of line position
		for x in xrange(self.size[0]):
			for y in xrange(self.size[1]):
				if self._map_ground[x][y] == MapModel.LINE_SYMBOL:
					self._line.append((x, y))
		i = 0
		for x in xrange(self.size[0]):
			for y in xrange(self.size[1]):
				for symbol in MapModel.BRAIN_SYMBOLS:					
					if self._map_ground[x][y] == symbol:
						logging.info("Initializing car #%d with %s brain"
									 % (i, MapModel.BRAIN_SYMBOLS[symbol]))
						i += 1
						heading = self._find_starting_heading((x, y))
						image = conf['resources']['game']['tiles']['cars'][
							MapModel.BRAIN_SYMBOLS[symbol]]
						# start at the middle of the case
						initPos = (x * conf['resources']['game']['tile_size'], 
							y * conf['resources']['game']['tile_size'])  
						self._cars.append(Car(
							initHeading=heading, image=image, initPos=initPos,
							objectName="Car-%s-%d" % (
								MapModel.BRAIN_SYMBOLS[symbol], i)))
						# replace the symbol by the tarmac symbol for further 
						# drawings
						self._map_ground[x][y] = MapModel.TARMAC_SYMBOL

		# the tiles will be drawn on this surface once, then this surface will
		# be drawn on the screen each frame
		self._map_surface = None

	def _find_starting_heading(self, pos):
		if len(self._line) == 0:
			raise Exception("Unable to find any starting line!")
		closest = (
			self._line[0][0], self._line[0][1])

		for line_pos in self._line:
			logging.info("New dist for %s is %s"
				% (str(line_pos), str(line_pos[0] * pos[0] + line_pos[1] * pos[1])))
			if square(line_pos[0] - pos[0]) + square(line_pos[1] - pos[1]) < \
					square(closest[0] - pos[0]) + square(closest[1] - pos[1]):
				closest = line_pos

		logging.info("Closest to %s among %s is %s"
					 % (str(pos), str(self._line), str(closest)))
		return (closest[0] - pos[0], closest[1] - pos[1])

	@property
	def name(self):
	    return self._static_data['name']
	@name.setter
	def name(self, value):
	    self._static_data['name'] = value

	@property
	def description(self):
	    return self._static_data['description']
	@description.setter
	def description(self, value):
	    self._static_data['description'] = value

	@property
	def nbCars(self):
	    return self._static_data['nb_cars']
	@nbCars.setter
	def nbCars(self, value):
	    self._static_data['nb_cars'] = value

	@property
	def size(self):
	    return self._static_data['size']
	@size.setter
	def size(self, value):
	    self._static_data['size'] = value

	@property
	def nbLaps(self):
	    return self._static_data['nb_laps']
	@nbLaps.setter
	def nbLaps(self, value):
	    self._static_data['nb_laps'] = value

	def getTile(self, pos):
		if self._map_ground[pos[0]][pos[1]] in self._tiles:
			return self._tiles[self._map_ground[pos[0]][pos[1]]]
		else:
			return None   # probably one of the cars, FIXME
	
	@property
	def cars(self):
	    return self._cars
	
	@property
	def mapSurface(self):
	    return self._map_surface
	def initMapSurface(self):
		self._map_surface = pygame.Surface(
			(self.size[0] * conf['resources']['game']['tile_size'],
			 self.size[1] * conf['resources']['game']['tile_size']),
			flags=pygame.HWSURFACE)
	
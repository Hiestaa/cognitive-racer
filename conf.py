# -*- coding: utf8 -*-

import logging
import math

conf = {
	'name': 'Racer',
	'state': 'DEBUG',
	'game_engine': {
		'update_time_step': 0.02,
		'simulate_hardware_lag': 0,
		'car': {
			'default_constants': {
				'acceleration': 0.05,
				'break': 0.1,
				'max_speed': 1,
				'maniability': math.pi / 360 * 10
			}
		}
	},
	'logging': {
		'log_file_level': logging.INFO,
		'log_console_level': 0
	},
	'graphx': {
		'screen_size': (1280, 800),
		'screen_base_color': (0, 0, 0),
		'video_player': {
			'max_fps': 60
		},
		'font': 'None'
	},
	'events': {
		'key_repeat_delay': 200,
		'key_repeat_interval': 1
	},
	'resources': {
		'font': {
			'default': 'resources/font/amaranth/Amaranth-Regular.ttf',
			'system': 'bitstreamverasans',
			'use_system': True,
			'default_precision': 32
		},
		'game': {
			'default_game_object': 'resources/game/default-game-object.png',
			'tiles': {
				'grass': 'resources/game/grass-tile.png',
				'tarmac': 'resources/game/tarmac-tile.png',
				'line': 'resources/game/line-tile.png',
				'cars': {
					'human': 'resources/game/cars/human-brain-tile.png'
				}
			},
			'default_map': 'resources/maps/base.json',
			'tile_size': 10
		},
		'language': 'fr'
	}
}
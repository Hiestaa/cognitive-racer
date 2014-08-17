#!/usr/local/bin/python

import pygame
from pygame.locals import *
import time

def init():
	pygame.display.set_mode((800, 600))



def test_1():
	def test(pressed, i):
		if i == 0:
			return
		if pressed[K_a]:
			print "K_a"
		if pressed[K_b]:
			print "K_b"
		test(pressed, i -1)
	pressed = pygame.key.get_pressed()
	for x in xrange(10000):
		# test 2 differents keys
		test(pressed, 100)

def test_2():
	def test(i):
		pressed = pygame.key.get_pressed()
		if i == 0:
			return
		if pressed[K_a]:
			print "K_a"
		if pressed[K_b]:
			print "K_b"
		test(i -1)
	for x in xrange(10000):
		# test 2 differents keys
		test(100)

def bench(init, funclist):
	init()
	for f in funclist:
		t0 = time.time()
		f()
		elapsed = time.time() - t0
		print "Function: %s took: %.5fs" % (f.__name__, elapsed)
			
if __name__ == '__main__':
	bench(init, [test_1, test_2])

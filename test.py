import pygame

from Graphx import graphx

graphx.init()

texture = pygame.image.load('resources/game/grass-tile.png')
degree = 0

while True:
    degree += 0.5
    if degree > 360:
        degree = 0
    rotTexture = pygame.transform.rotate(texture, degree)
    rect = rotTexture.get_rect()
    rect.center = 100, 100
    print rotTexture.get_rect()
    graphx.draw(rotTexture, rect)
    graphx.update()

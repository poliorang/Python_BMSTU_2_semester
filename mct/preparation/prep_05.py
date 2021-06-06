## шестиугольники по параболе из вулкана
import pygame
from math import *

x = 1
phi = 1
g = 10
v = 1

FPS = 6
# six = [[300, 300], [340, 3200], [380, 260], [340, 220], [300, 220], [260, 260]]
six = [[300, 300], [320, 300], [340, 280], [320, 260], [300, 260], [280, 280]]

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('white')

    pygame.draw.arc(screen, 'black', [330, 300, 200, 60], 0, 2*pi, 5)
    pygame.draw.line(screen, 'black', [330, 330], [120, 600], 5)
    pygame.draw.line(screen, 'black', [530, 330], [730, 600], 5)

    pygame.draw.polygon(screen, 'brown', six)
    x -= 1
    y = x**2 / 6 - 10

    for i in range(6):
        six[i] = [six[i][0] + v, six[i][1] + y]
    pygame.display.update()

pygame.quit()
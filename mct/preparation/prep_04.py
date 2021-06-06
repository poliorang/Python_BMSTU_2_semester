## вращение аля бильярдной расстановки шаров (сверху треугольник) вокруг центра уголового круга
import pygame
from math import *

FPS = 60
center = [500, 300]
phi = radians(1)

c1 = [500, 300]
c2 = [440, 300]
c3 = [380, 300]
c4 = [470, 250]
c5 = [410, 250]
c6 = [440, 200]

def rotate(coord, center, phi):
    coord = coord[0] - center[0], coord[1] - center[1]
    coord = (cos(phi) * coord[0] - sin(phi) * coord[1], sin(phi) * coord[0] + cos(phi) * coord[1])
    coord = coord[0] + center[0], coord[1] + center[1]
    return coord

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

    pygame.draw.circle(screen, 'brown', c1, 30)
    pygame.draw.circle(screen, 'pink', c2, 30)
    pygame.draw.circle(screen, 'purple', c3, 30)

    pygame.draw.circle(screen, 'purple', c4, 30)
    pygame.draw.circle(screen, 'brown', c5, 30)

    pygame.draw.circle(screen, 'pink', c6, 30)

    c1 = rotate(c1, center, phi)
    c2 = rotate(c2, center, phi)
    c3 = rotate(c3, center, phi)
    c4 = rotate(c4, center, phi)
    c5 = rotate(c5, center, phi)
    c6 = rotate(c6, center, phi)

    pygame.display.update()

pygame.quit()
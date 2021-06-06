## прямоугольник вращается относительно нижней вершины, внутри него круг, все масштабируется
import pygame
from math import *

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

figure = [[450, 150], [450, 250], [500, 250], [500, 150]]
cir = [475, 200]
center = [500, 150]
rad = 20

k = 1.001

pygame.init()
screen = pygame.display.set_mode((900, 370))
clock = pygame.time.Clock()

def rotate(coord, phi, center):
    coord = coord[0] - center[0], coord[1] - center[1]
    coord = (cos(phi) * coord[0] - sin(phi) * coord[1], sin(phi) * coord[0] + cos(phi) * coord[1])
    coord = coord[0] + center[0], coord[1] + center[1]
    return coord

def resize(coord, k, center):
    coord = coord[0] - center[0], coord[1] - center[1]
    coord = (coord[0] * k, coord[1] * k)
    coord = coord[0] + center[0], coord[1] + center[1]
    return coord

run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(WHITE)
    pygame.draw.polygon(screen, BLACK, figure)
    pygame.draw.circle(screen, RED, cir, rad)

    phi = radians(1)

    for i in range(4):
        figure[i] = rotate(figure[i], phi, center)
        figure[i] = resize(figure[i], k, center)

    rad *= k
    cir = rotate(cir, phi, center)
    cir = resize(cir, k, center)

    pygame.display.update()

pygame.quit()
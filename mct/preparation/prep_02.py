## равносторонний треугольник вращается вокруг своего центра тяжести
import pygame
from math import *

FPS = 60 # Frames Per Second
WIDTH = 900
HEIGHT = 576
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 1
speed = 1

triagle = [[100, 200], [40, 300], [160, 300]]
center = [100, 267]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def rotate(coord, phi):
    rot = (cos(phi) * coord[0] + sin(phi) * coord[1], - sin(phi) * coord[0] + cos(phi) * coord[1])
    return rot


run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(WHITE)
    pygame.draw.polygon(screen, BLACK, triagle)

    phi = radians(1)

    for i in range(3):
        triagle[i] = (triagle[i][0] - center[0], triagle[i][1] - center[1])
        triagle[i] = rotate(triagle[i], phi)
        triagle[i] = (triagle[i][0] + center[0], triagle[i][1] + center[1])

    pygame.display.flip()

pygame.quit()

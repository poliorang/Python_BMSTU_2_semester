## равносторонний треугольник вращается вокруг своего центра тяжести и движется по синусоиде
import pygame
from math import *

FPS = 60 # Frames Per Second
WIDTH = 900
HEIGHT = 576
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 1
speed = 1

triagle = [[0, 200], [-60, 300], [60, 300]]
center = [0, 267]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def rotate(coord, phi):
    rot = (cos(phi) * coord[0] - sin(phi) * coord[1], sin(phi) * coord[0] + cos(phi) * coord[1])
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
    x += 1
    y = sin(radians(x)) * speed

    for i in range(3):
        triagle[i] = [triagle[i][0] + speed, triagle[i][1] + y]

    center = [center[0] + speed, center[1] + y]

    for i in range(3):
        triagle[i] = (triagle[i][0] - center[0], triagle[i][1] - center[1])
        triagle[i] = rotate(triagle[i], phi)
        triagle[i] = (triagle[i][0] + center[0], triagle[i][1] + center[1])

    pygame.display.flip()

pygame.quit()

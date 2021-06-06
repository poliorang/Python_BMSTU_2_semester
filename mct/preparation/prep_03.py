## круг, поделенный на разноцветные сектора, вращается по часовой стрелке и двигается от края до края по синусоиде
import pygame
from math import *
FPS = 200

x = 1
phi = 0
center = [100, 300]
coord = [50, 50, 300, 300]
flag = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((990, 600))

def rotate(coord, center, phi):
    coord = coord[0] - center[0], coord[1] - center[1]
    coord = (cos(phi) * coord[0] - sin(phi) * coord[1], sin(phi) * coord[0] + cos(phi) * coord[1])
    coord = coord[0] + center[0], coord[1] + center[1]
    return coord

coord_start = [50, 50, 300, 300]

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x += 1
    if not x % 600:
        flag += 1

    y = sin(radians(x))*40
    phi -= radians(1)

    screen.fill('white')

    if flag % 2:
        coord[0] -= 1
    else:
        coord[0] += 1
    coord[1] = coord_start[1] + y

    pygame.draw.arc(screen, 'pink', coord, 0 + phi, pi / 2 + phi, 220)
    pygame.draw.arc(screen, 'black', coord, pi / 2 + phi, pi + phi, 220)
    pygame.draw.arc(screen, 'purple', coord, pi + phi, 3 * pi / 2 + phi, 220)
    pygame.draw.arc(screen, 'grey', coord, 3 * pi / 2 + phi, 2 * pi + phi, 220)

    pygame.display.flip()

pygame.quit()

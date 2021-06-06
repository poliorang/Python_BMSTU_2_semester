import pygame
from math import *

def rotate(img, coords, phi1):
    w, h = img.get_size()
    a0 = atan(w / h)
    a01 = atan(h / w)
    d = (w ** 2 + h ** 2) ** 0.5
    comp0_x, comp0_y = coords
    rot_img = pygame.transform.rotate(img, phi1)
    phi = phi1 % -90
    phi_r = -radians(phi)
    comp_x = d * sin(phi_r / 2) * cos((2 * a0 + phi_r) / 2)
    comp_y = d * sin((2 * a0 - phi_r) / 2) * sin(phi_r / 2)

    if phi == 0:
        a0, a01 = a01, a0
        comp0_x -= comp_x
        comp0_y -= comp_y

    screen.blit(rot_img, (round(comp0_x - comp_x), round(comp0_y - comp_y)))

def ball_go():
    global x, y, angle, flag_up_down
    speed = 5
    comp = 2
    angle -= speed * 1.57

    pos = (x, y + comp)
    rotate(ball, pos, angle)

    if flag_up_down:
        # вверх
        y -= speed
    else:
        # вниз
        y += speed

FPS = 50 # Frames Per Second
WIDTH = 626
HEIGHT = 576
WHITE = (255, 255, 255)
RED = (255, 0, 0)


#анимация
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My animation")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# картиночки
bg = pygame.image.load('pictures/field.jpg').convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

foot_1_1 = pygame.image.load('pictures/1_1.png').convert()
foot_1_1 = pygame.transform.scale(foot_1_1, (430, 200))
foot_1_2 = pygame.image.load('pictures/1_2.png').convert()
foot_1_2 = pygame.transform.scale(foot_1_2, (430, 200))
foot_1_3 = pygame.image.load('pictures/1_3.png').convert()
foot_1_3 = pygame.transform.scale(foot_1_3, (430, 200))
foot_1_4 = pygame.image.load('pictures/1_4.png').convert()
foot_1_4 = pygame.transform.scale(foot_1_4, (430, 200))

foot_2_1 = pygame.image.load('pictures/2_1.png').convert()
foot_2_2 = pygame.image.load('pictures/2_2.png').convert()
foot_2_3 = pygame.image.load('pictures/2_3.png').convert()
foot_2_4 = pygame.image.load('pictures/2_4.png').convert()

ball = pygame.image.load('pictures/ball.png').convert()
ball = pygame.transform.scale(ball, (40, 40))

# пайгейм дурачок и не знает, что такое прозрачный фон, поэтому:
foot_1_1.set_colorkey(WHITE)
foot_1_2.set_colorkey(WHITE)
foot_1_3.set_colorkey(WHITE)
foot_1_4.set_colorkey(WHITE)

foot_2_1.set_colorkey(WHITE)
foot_2_2.set_colorkey(WHITE)
foot_2_3.set_colorkey(WHITE)
foot_2_4.set_colorkey(WHITE)

ball.set_colorkey(RED)


# игровой цикл
run = True
flag_up_down = 1
x = 290
y = 425
angle = 50
count = 0

while run:
    # частота кадров
    clock.tick(FPS)
    # для удержания открытого приложения
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # обновление фона
    screen.blit(bg, (0, 0))

    if y > 99 and flag_up_down == 1:
        #смена игрока
        if y == 100:
            count += 1
        #мерцающие
        screen.blit(foot_2_1, (155, 320))
        screen.blit(foot_1_1, (0, 350))
        ball_go()
    else:
        flag_up_down = 0

    if y <= 425 and flag_up_down == 0:
        if count % 2 == 0:
            if 99 <= y <= 360:
                screen.blit(foot_2_1, (155, 320))
                screen.blit(foot_1_1, (0, 350))
            if 360 <= y <= 380:
                screen.blit(foot_1_2, (0, 350))
                screen.blit(foot_2_1, (155, 320))
            if 380 <= y <= 400:
                screen.blit(foot_1_3, (0, 350))
                screen.blit(foot_2_1, (155, 320))
            if 400 <= y <= 440:
                screen.blit(foot_1_4, (0, 350))
                screen.blit(foot_2_1, (155, 320))
        else:
            if 99 <= y <= 360:
                screen.blit(foot_1_1, (0, 350))
                screen.blit(foot_2_1, (155, 320))
            if 360 <= y <= 380:
                screen.blit(foot_2_2, (155, 320))
                screen.blit(foot_1_1, (0, 350))
            if 380 <= y <= 400:
                screen.blit(foot_2_3, (155, 320))
                screen.blit(foot_1_1, (0, 350))
            if 400 <= y <= 440:
                screen.blit(foot_2_4, (155, 320))
                screen.blit(foot_1_1, (0, 350))
        ball_go()
    else:
        flag_up_down = 1

    pygame.display.flip()

pygame.quit()
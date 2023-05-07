import sys
import pygame
from pygame.draw import *

pygame.init()
w = 800  # Ширина экрана
h = 600  # Высота экрана
fps = 60
screen = pygame.display.set_mode((w, h))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (125, 125, 125)
light_blue = (64, 128, 255)
green = (0, 200, 64)
yellow = (225, 225, 0)
pink = (230, 50, 230)
red = (255, 0, 0)

right = "to the right"
left = "to the left"
up = "to the up"
down = "to the down"
stop = "stop"
motion = stop
# Координаты и радиус круга
x = w // 2
y = h // 2
r = 50

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                motion = left
            elif event.key == pygame.K_RIGHT:
                motion = right
            elif event.key == pygame.K_UP:
                motion = up
            elif event.key == pygame.K_DOWN:
                motion = down
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = stop

    screen.fill([125, 125, 125])
    pygame.draw.circle(screen, green, (x, y), r)
    pygame.display.update()

    if motion == left:
        x -= 3
    elif motion == right:
        x += 3
    elif motion == up:
        y -= 3
    elif motion == down:
        y += 3

    clock.tick(fps)

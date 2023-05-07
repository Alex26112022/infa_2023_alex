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
                x -= 3
            elif event.key == pygame.K_RIGHT:
                x += 3
            elif event.key == pygame.K_UP:
                y -= 3
            elif event.key == pygame.K_DOWN:
                y += 3
    screen.fill([125, 125, 125])
    pygame.draw.circle(screen, green, (x, y), r)
    pygame.display.update()
    clock.tick(fps)

import sys
import pygame
from pygame.draw import *
import random

pygame.init()
w = 1520  # Ширина экрана
h = 800  # Высота экрана
fps = 60
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

white = [255, 255, 255]
black = [0, 0, 0]
gray = [125, 125, 125]
light_blue = [64, 128, 255]
green = [0, 200, 64]
yellow = [225, 225, 0]
pink = [230, 50, 230]
red = [255, 0, 0]
screen.fill(light_blue)

# Параметры шаров
x = random.randint(40, 1480)
y = random.randint(40, 760)
r = random.randint(5, 80)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.circle(screen, red, (x, y), r)
    pygame.display.update()
    clock.tick(fps)

import sys
import pygame
from pygame.draw import *
import random

pygame.init()
w = 800  # Ширина экрана
h = 600  # Высота экрана
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

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(light_blue)
    pygame.display.update()
    clock.tick(fps)

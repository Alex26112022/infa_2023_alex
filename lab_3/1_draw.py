import sys

import pygame
from pygame.draw import *


def main():
    pygame.init()
    fps = 30
    screen = pygame.display.set_mode((800, 600))
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (125, 125, 125)
    light_blue = (64, 128, 255)
    green = (0, 200, 64)
    yellow = (225, 225, 0)
    pink = (230, 50, 230)

    def png_1():
        """ Рисует картинку. """
        pass

    png_1()

    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()

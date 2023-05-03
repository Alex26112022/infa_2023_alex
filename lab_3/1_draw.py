import sys

import pygame
from pygame.draw import *


def main():
    pygame.init()
    fps = 30
    screen = pygame.display.set_mode((800, 600))

    def png_1():
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

import sys
import pygame
from pygame.draw import *


def main():
    pygame.init()
    fps = 30
    screen = pygame.display.set_mode((800, 600))
    screen.fill([125, 125, 125])
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (125, 125, 125)
    light_blue = (64, 128, 255)
    green = (0, 200, 64)
    yellow = (225, 225, 0)
    pink = (230, 50, 230)

    def png_1():
        """ Рисует картинку. """

        def head():
            """ Рисует голову. """
            pygame.draw.circle(screen, yellow, (400, 300), 200)
            pygame.draw.circle(screen, black, (400, 300), 200, 2)

        def brows():
            """ Рисует брови. """
            x_l1 = 250  # координата х левого края левой брови
            y_l1 = 250  # координата у левого края левой брови
            x_l2 = 350  # координата х правого края левой брови
            y_l2 = 200  # координата у правого края левой брови
            x_r1 = 450  # координата х левого края правой брови
            y_r1 = 200  # координата у левого края правой брови
            x_r2 = 550  # координата х правого края правой брови
            y_r2 = 250  # координата у правого края правой брови
            pygame.draw.line(screen, black, (x_l1, y_l1), (x_l2, y_l2), 20)  # левая бровь
            pygame.draw.line(screen, black, (x_r1, y_r1), (x_r2, y_r2), 20)  # правая бровь

        def eyes():
            """ Рисует глаза. """
            r_l1 = 40  # радиус левого глаза
            r_l2 = 10  # радиус зрачка левого глаза
            r_r1 = 30  # радиус правого глаза
            r_r2 = 15  # радиус зрачка правого глаза
            pygame.draw.circle(screen, pink, (300, 300), r_l1)  # левый глаз
            pygame.draw.circle(screen, black, (300, 300), r_l1, 2)  # контур левого глаза
            pygame.draw.circle(screen, black, (300, 300), r_l2)  # зрачок левого глаза
            pygame.draw.circle(screen, pink, (500, 300), r_r1)  # правый глаз
            pygame.draw.circle(screen, black, (500, 300), r_r1, 2)  # контур правого глаза
            pygame.draw.circle(screen, black, (500, 300), r_r2)  # зрачок правого глаза

        def mouth():
            """ Рисует рот. """
            rect(screen, black, (280, 370, 250, 50))  # координаты х, у левого верхнего края, ширина, высота

        head()
        brows()
        eyes()
        mouth()

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

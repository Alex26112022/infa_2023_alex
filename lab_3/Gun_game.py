import pygame
from pygame.draw import *
import random

pygame.init()
w = 1520  # Ширина экрана
h = 800  # Высота экрана
fps = 1
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Игра ПОЙМАЙ ШАРИК')
img = pygame.image.load('кролик4.jpeg')
clock = pygame.time.Clock()

white = [255, 255, 255]
black = [0, 0, 0]
gray = [125, 125, 125]
light_blue = [64, 128, 255]
green = [0, 200, 64]
yellow = [225, 225, 0]
pink = [230, 50, 230]
red = [255, 0, 0]
colors = [white, black, gray, light_blue, green, yellow, pink, red]
screen.blit(img, (-100, -50))  # копирует пиксели загруженного изображения на фон, значения смещают по х, у


# screen.fill(light_blue)


def draw_circle():
    """ Рисует шары. """
    global x, y, r
    x = random.randint(40, 1480)
    y = random.randint(40, 760)
    r = random.randint(5, 80)
    color = colors[random.randint(0, 7)]
    circle(screen, color, (x, y), r)


def click():
    """ Определяет попадание. """
    # if (event.x - x) ** 2 + (event.y - y) ** 2 <= r ** 2:
    #     print('Молодец, попал!!!')
    # else:
    #     print('Мимо, целься лучше!')
    print(x, y, r)


finished = True
pygame.display.update()

while finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!', event.pos)

    draw_circle()
    click()
    pygame.display.update()
    screen.blit(img, (-100, -50))  # копирует пиксели загруженного изображения на фон, значения смещают по х, у

quit()

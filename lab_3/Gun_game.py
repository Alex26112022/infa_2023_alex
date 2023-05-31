import pygame
from pygame.draw import *
from random import randint

pygame.init()
w = 1520  # Ширина экрана
h = 800  # Высота экрана
fps = 1
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Игра ПОЙМАЙ ШАРИК')
clock = pygame.time.Clock()

white = [255, 255, 255]
black = [0, 0, 0]
gray = [125, 125, 125]
light_blue = [64, 128, 255]
green = [0, 200, 64]
yellow = [225, 225, 0]
pink = [230, 50, 230]
red = [255, 0, 0]
colors = [white, gray, black, green, yellow, pink, red]
# screen.blit(img, (0, 0))  # копирует пиксели загруженного изображения на фон, значения смещают по х, у


screen.fill(light_blue)


def draw_circle():
    """ Рисует шары. """
    global px, py, pr
    px = randint(40, 1480)
    py = randint(40, 760)
    pr = randint(5, 80)
    color = colors[randint(0, 6)]
    circle(screen, color, (px, py), pr)


finished = True
pygame.display.update()

while finished:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!', event.pos)
            if (event.pos[0] - px) ** 2 + (event.pos[1] - py) ** 2 <= pr ** 2:
                print('Молодец, попал!!!')
            else:
                print('Мимо, целься лучше!')
                print(px, py, pr)

    draw_circle()

    pygame.display.update()
    screen.fill(light_blue)
    # screen.blit(img, (0, 0))  # копирует пиксели загруженного изображения на фон, значения смещают по х, у

quit()

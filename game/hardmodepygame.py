import sys, pygame, pygame.mixer
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

#png

background = pygame.image.load("png/720bg.jpg").convert()
bulletpicture = pygame.image.load("png/arrow.png").convert_alpha()
logo= pygame.image.load("png/arrow.png")
#title

pygame.display.set_caption("hardmode","png/ship.png")
pygame.display.set_icon(logo)
clock = pygame.time.Clock()

bullets = []

background = pygame.image.load("png/720bg.jpg").convert()
bulletpicture = pygame.image.load("png/arrow.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            #shot.play()
            bullets.append([event.pos[0]-32, 500])

    clock.tick(60)
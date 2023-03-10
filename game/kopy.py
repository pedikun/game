import sys, pygame, pygame.mixer
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

bullets = []

background = pygame.image.load("png/arena.png").convert()
ship = pygame.image.load("png/ship.png").convert_alpha()
ship = pygame.transform.scale(ship, (64, 64))
bulletpicture = pygame.image.load("png/arrow.png").convert_alpha()

#shot = pygame.mixer.Sound("")
#soundin = pygame.mixer.Sound("")

#soundin.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            #shot.play()
            bullets.append([event.pos[0]-32, 500])

    clock.tick(60)
    #mouse get post
    mx, my = pygame.mouse.get_pos()
    #mouse get post
    for b in range(len(bullets)):
        bullets[b][0] -= 10

    # Iterate over a slice copy if you want to mutate a list.
    for bullet in bullets[:]:
        if bullet[0] < 0:
            bullets.remove(bullet)

    screen.blit(background, (0, 0))

    for bullet in bullets:
        screen.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))

    screen.blit(ship, (mx-32, 500))
    pygame.display.flip()
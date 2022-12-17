import sys, pygame, pygame.mixer
from pygame.locals import *

pygame.init()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

bullets = []
enemys  = []
scores  = 0
start   = 0

background = pygame.image.load("png/arenabutbetter.png").convert()
#ship = pygame.image.load("ship.png").convert_alpha()
#ship = pygame.transform.scale(ship, (64, 64))
bulletpicture = pygame.image.load("png/arrow144p.png").convert_alpha()
enemypicture  = pygame.image.load("png/enemy.png").convert_alpha()
#shot = pygame.mixer.Sound("shot.wav")
musick= pygame.mixer.Sound("mic/mus_zz_megalovania.ogg")
#soundin = pygame.mixer.Sound("sound.wav")
#soundin.play()

def e1():
    enemys.append([1000, 0  ])
def e2():
    enemys.append([1000, 144])
def e3():
    enemys.append([1000, 288])
def e4():
    enemys.append([1000, 432])
def e5():
    enemys.append([1000, 576])

def start_music():
    musick.play()
    
while True:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            #shot.play()
            if my > 0 and my < 144 :
                bullets.append([-100, 0])#([event.pos[0]-32, 0]) for further use
                
            elif my > 144 and my < 288: 
                bullets.append([-100, 144])
                
            elif my > 288 and my < 432: 
                bullets.append([-100, 288])
                
            elif my > 432 and my < 576: 
                bullets.append([-100, 432])
        #enemy testing
            elif my > 576 and my < 720: 
                bullets.append([-100, 576])
    #worked protype but bugged
    key_press = pygame.key.get_pressed()
    if key_press[K_SPACE]:
        enemys.append([1000, 576])
        #start_music()
        start +=1
        if start ==1 :
            start_music()
    #worked protype but bugged
        
    clock.tick(60)
    #triger test
    #delay = pygame.time.delay()
    
    #triget test
    
    #for score in scores:
        
#this one for the bullet physick
    for b in range(len(bullets)):
        bullets[b][0] += 10
        
    for e in range(len(enemys)) :
        enemys[e][0]  -= 10

    
    # Iterate over a slice copy if you want to mutate a list. v this for delete bullet currently delete at 0/0
    for bullet in bullets[:]:
        if bullet[0] > 1280:
            bullets.remove(bullet)
    
    for enemy in enemys[:]  :
        if enemy[0] < -100:
            enemys.remove(enemy)

    screen.blit(background, (0, 0))

    for bullet in bullets:
        screen.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))

    for enemy in enemys:
        screen.blit(enemypicture, pygame.Rect(enemy[0],enemy[1], 0, 0))
    
    #screen.blit(ship, (mx-32, 500))
    pygame.display.flip()
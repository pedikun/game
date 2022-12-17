import sys, pygame, pygame.mixer
from pygame.locals import *

wn =pygame.display.set_mode((1280,720))
pygame.display.set_caption("hard mode")

background = pygame.image.load("png/720bg.jpg").convert()
arrow= pygame.image.load("png/arrow.png").convert_alpha()
cube= pygame.image.load("png/cube.png").convert()

pain=[]

clock = pygame.time.Clock()

def draw():
    #wn.fill((30,30,30))
    wn.blit(cube,(0,355))
    pygame.display.flip()
    
def boolet():
    for b in range(len(pain)):
        pain[b][0] -= 10
        
    for bullet in pain[:]:
        if bullet[0] < 0:
            pain.remove(bullet)
            
    wn.blit(background,(0,0))
    
    
    for bullet in pain:
        wn.blit(arrow, pygame.Rect(bullet[0], bullet[1], 0, 0))
    

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                #shot.play()
                pain.append([event.pos[0]-32, 500])
                
        boolet()
        
        draw()

if __name__ == "__main__":
    main()
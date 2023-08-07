import pygame
pygame.init()
WIDTH=400
HEIGHT=500
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
x=20
y=20
screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('My first pygame win')
running=True
while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_a:
                x -= 10
            if event.key==pygame.K_w:
                y -= 10
            if event.key==pygame.K_s:
                y += 10
            if event.key==pygame.K_d:
                x += 10
    screen.fill(BLUE)
    pygame.draw.rect(screen,GREEN,(x,y,50,50))
    
    pygame.display.update()

pygame.quit()
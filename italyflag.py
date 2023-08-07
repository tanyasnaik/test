import pygame
pygame.init()
screen=pygame.display.set_mode([900,600])
pygame.display.set_caption('Italy flag')
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((244, 245, 240))
    pygame.draw.rect(screen,(0, 140, 69),(0,0,300,900)) 
    pygame.draw.rect(screen,(205, 33, 42),(600,0,300,900))

    pygame.display.update()

pygame.quit()
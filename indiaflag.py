import pygame
pygame.init()
screen=pygame.display.set_mode([900,600])
pygame.display.set_caption('India flag')
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0, 0, 128),(450,300),80)
    pygame.draw.rect(screen,(255, 119, 34),(0,0,900,200)) 
    pygame.draw.rect(screen,(19, 136, 8),(0,400,900,200))

    pygame.display.update()

pygame.quit()
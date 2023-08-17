import pygame
import time
import random

pygame.init()
WIDTH=800
HEIGHT=500
RED=(199, 0, 57)
GREEN=(48, 169, 54)
BLUE=(103, 193, 255)
YELLOW=(255, 195, 0)
WHITE=(255,255,255)


snakesize=10
snakelist=[]
snakelength=1

clock=pygame.time.Clock()
screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('My first pygame win')

font_style=pygame.font.SysFont('Felix Titling',20)
score_style=pygame.font.SysFont('Papyrus',15)

def message(msg,color,xco,yco):
    mesg=font_style.render(msg,True,color)
    screen.blit(mesg,[xco,yco])

def urscore(msg,color,xco,yco):
    mesg=score_style.render(msg,True,color)
    screen.blit(mesg,[xco,yco])

def gameloop():
    x=0
    y=0
    x_new=300
    y_new=300
    gameover=False
    gameclose=False
    foodx= round(random.randrange(0,WIDTH-snakesize)/10.0)*10.0
    foody=round(random.randrange(0,HEIGHT-snakesize)/10.0)*10.0

    while  not gameover:
        while gameclose == True:
            screen.fill(WHITE)
            message('Game over.\nPress Q to quit or C to play again!',RED,30,30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameclose=False
                        gameover=True
                    if event.key==pygame.K_c:
                        gameloop()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x -= 10
                    y=0
                if event.key==pygame.K_UP:
                    y -= 10
                    x=0
                if event.key==pygame.K_DOWN:
                    y += 10
                    x=0
                if event.key==pygame.K_RIGHT:
                    x += 10
                    y=0
        
        x_new=x_new+x
        y_new=y_new+y    
        if x_new > WIDTH or x_new < 0 or y_new > HEIGHT or y_new <0:
            gameclose=True

        screen.fill(BLUE)       
        pygame.draw.rect(screen,GREEN,(x_new,y_new,snakesize,snakesize))
        snakehead=[]
        snakehead.append(x_new)
        snakehead.append(y_new)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]

        for x in snakelist[:-1]:
            if x==snakehead:
                gameclose=True
            
        oursnake(snakesize,snakelist)

        
        pygame.draw.rect(screen,YELLOW,(foodx,foody,snakesize,snakesize))
        if foodx==x_new and foody==y_new:
            foodx= round(random.randrange(0,WIDTH-snakesize)/10.0)*10.0
            foody=round(random.randrange(0,HEIGHT-snakesize)/10.0)*10.0
        urscore('Score: ',RED,15,15)
        pygame.display.update()
        clock.tick(10)

    pygame.quit()
    quit()

gameloop()
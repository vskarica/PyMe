#rect1.colliderect(rect2)
#rect1.collidepoint(x,y)

import pygame,sys

pygame.init()
clock=pygame.time.Clock()
screen_wh=screen_w,screen_h=800,400
screen=pygame.display.set_mode(screen_wh)

class myRect:
    def __init__(self, x,y, w,h, c,sx,sy):
        self.rect=pygame.Rect(x,y,w,h)
        self.speedX=sx
        self.speedY=sy
        self.c=c
    def draw(self,scr):
        pygame.draw.rect(scr,self.c,self.rect)
    def draw_next(self,scr):
        self.rect.x+=self.speedX
        self.rect.y+=self.speedY
        self.draw(scr)

class stuf:
    lista=[]
    def nacrtaj_sve(screen):
        for ob in stuf.lista:
            ob.draw(screen)
def border_bounce(r1):
    if(r1.rect.right>screen_w):
        r1.speedX*=-1
        r1.rect.right=screen_w
    if(r1.rect.left<0):
        r1.speedX*=-1
        r1.rect.left=0
    if(r1.rect.bottom>screen_h):
        r1.speedY*=-1
        r1.rect.bottom=screen_h
    if(r1.rect.top<0):
        r1.speedY*=-1
        r1.rect.top=0
def bouncing_rect():
    border_bounce(rect1)
    border_bounce(rect2)

    cllision_tolerance=15
    if rect1.rect.colliderect(rect2.rect):
        tb=rect1.rect.top-rect2.rect.bottom
        bt=rect1.rect.bottom-rect2.rect.top
        rl=rect1.rect.right-rect2.rect.left
        lr=rect1.rect.left-rect2.rect.right
        if abs(tb)<cllision_tolerance:
            rect1.speedY*=-1
            rect1.rect.y-=tb
        if abs(bt)<cllision_tolerance:
            rect1.speedY*=-1
            rect1.rect.y-=bt
        if abs(lr)<cllision_tolerance:
            rect1.speedX*=-1
            rect1.rect.x-=lr
        if abs(rl)<cllision_tolerance:
            rect1.speedX*=-1
            rect1.rect.x-=rl

    rect1.draw_next(screen)
    rect2.draw_next(screen)

rect1=myRect(350,350,100,100,(255,255,255),4,10)
rect2=myRect(300,600,200,100,(255,  0,  0),0,4)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(120)


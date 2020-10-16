import sys, pygame
from myGameClasees import *
from tinydb import TinyDB, Query
import math
from random import randrange, choice
#import numpy as np
db = TinyDB( 'rObjects.json' )

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10)

frames_per_second=24
main_loop_index=0   
screenSize = ( 600, 300 )
monitorSize=[pygame.display.Info().current_w,pygame.display.Info().current_h]
fullScr=False
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
black=0,0,0
blue=0,0,255
#"""
#muzika = pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.play(-1)
#"""
pogodak = pygame.mixer.Sound("hit.wav")

class room:
    roomSize=0,0
    objList=[]
    name=""
    def __init__ ( self, name, roomSize = (0,0)):
        self.name=name
        self.roomSize=roomSize

class rObject:
    x=0
    y=0
    roundX=0
    roundY=0
    destX=x
    destY=y
    radius=0
    speed=10
    width=0
    height=0
    icon=0
    def __init__(self,x=0,y=0,radius=0):
        self.radius=radius
        self.x=x
        self.y=y
        self.roundX=x
        self.roundY=y
        self.destX=x
        self.destY=y
        db.insert({'ime':'Mate', 'bodovi':0})
        class igra:
            pass
        class soba:
            pass
        class sloj:
            pass
        class objekt:
            pass
        class slika:
            pass
        igra.sobe=[]
        igra.sobe.append(soba())
        igra.sobe.append(soba())
        igra.sobe[0].val=1
        igra.sobe[1].val=2
        #print(igra.sobe[0].val)
    def moveOneStep(self):
        
        if(self.destX!=self.x or self.destY!=self.y):
            vector=self.vectorDiffrance(self.destX,self.destY,self.x,self.y)
            d=self.udaljenostTocaka(self.x,self.y,self.destX,self.destY)
            if(d<self.speed):
                self.x=self.destX
                self.y=self.destY
            else:
                vectorXj=vector[0]/d
                vectorYj=vector[1]/d
                self.x+=vectorXj*self.speed
                self.y+=vectorYj*self.speed
                self.roundX=round(self.x)
                self.roundY=round(self.y)

            
    def place(self):
        return self.roundX,self.roundY

    def vectorDiffrance(self,x1,y1,x2,y2):
        return x1-x2,y1-y2
        
    def udaljenostTocaka(self,x1,y1,x2,y2):
        xx=max(x1,x2)-min(x1,x2)
        yy=max(y1,y2)-min(y1,y2)
        return math.sqrt(xx**2+yy**2)
        
def udaljenostTocaka(x1,y1,x2,y2):
    xx=max(x1,x2)-min(x1,x2)
    yy=max(y1,y2)-min(y1,y2)
    return math.sqrt(xx**2+yy**2)
    
def resize(aaaa,aaaaa,*screen):
    screen = pygame.display.set_mode(aaaa, aaaaa)


#https://prod.liveshare.vsengsaas.visualstudio.com/join?1BA576DACCB0FF1D6630B4FCC06104F17241
class icon:
    radius=0

MainLoop=True
soba1=room("soba1")
rooms=[]
rooms.append(soba1)
#a=room("prva soba",(600,300))
#print(a.name)


rObjekt1=rObject(300,200,100)
rObjekt2=rObject(150,30,50)
rObjekt3=rObject(98,65,50)
rObjekt4=rObject(550,260,50)
rObjekt5=rObject(122,244,50)

def inputObj():
    rooms[0].objList.append(rObjekt1)
    rooms[0].objList.append(rObjekt2)
    rooms[0].objList.append(rObjekt3)
    rooms[0].objList.append(rObjekt4)
    rooms[0].objList.append(rObjekt5)
inputObj()

def drawBackgroundNet(
    surface,
    info={
        "x":0,
        "y":0,
        "distance":50
        }):
    x=round(info["x"])  #211                   #pomak mreže
    y=round(info["y"])
    distance=info["distance"]             #veličina očice u px
    font='Comic Sans MS'
    fsize=10
    myGridFont = pygame.font.SysFont(font, fsize)
    w, h = pygame.display.get_surface().get_size()
    wh=max(w,h)
    nW=w//distance+1        #broj crta u širinu
    nH=h//distance+1        #broj crta u visinu
    #i0=-x//distance         #broj prve crte
    #i1=(wh-x)//distance     #broj zadnje crte

    for i in range(nW): #range(i0,i1+1):   #range(1,wh//distance+1):
        x0=x%distance   # x prve crte
        pygame.draw.line(surface, (0,100,0), (i*distance+x0,0), (i*distance+x0,h), 1)
        textsurface = myGridFont.render(str((i-x//distance)*distance), False, (0, 255, 0))
        surface.blit(textsurface,(i*distance+x0,0))

    for j in range(nH): #range(i0,i1+1):   #range(1,wh//distance+1):
        y0=y%distance   # y prve crte
        pygame.draw.line(surface, (0,100,0), (0,j*distance+y0), (w,j*distance+y0), 1)
        textsurface = myGridFont.render(str((j-y//distance)*distance), False, (0, 255, 0))
        surface.blit(textsurface,(0,j*distance+y0))

    pygame.draw.circle(surface, (255,0,0), (x,y), 10, 1)
    #print("grid:",i,j,x,y,x0,y0)

        
myGameClock=pygame.time.Clock();
fNotPressed=True
while MainLoop:
    main_loop_index+=1                      #inkrement indexa petlje
    
    myGameClock.tick(frames_per_second)     
    
    playerX=rooms[0].objList[0].x           #pojednostavljivanje igračevih x i y
    playerY=rooms[0].objList[0].y
    
    mouseXY=pygame.mouse.get_pos();

    if(main_loop_index % (frames_per_second / 2)==0):   #stvara nove objekte
        x=round(playerX)+choice((-1, 1))*randrange(150,300)
        y=round(playerY)+choice((-1, 1))*randrange(150,300)
        #x=randrange(-300,300)
        #y=randrange(-300,300) if 
        rooms[0].objList.append (rObject(x, y,50))
        print(x,y)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainLoop=False
            a=db.all()[0]
            print(a['ime'])
            #for item in db:
            #    print(item['ime'])
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_x:
                MainLoop=False
            if event.key == pygame.K_q:
                #e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
                e1 = pygame.event.Event(pygame.VIDEORESIZE,w=500,h=500)
                pygame.event.post(e1)
            if event.key == pygame.K_r:
                inputObj()
            if event.key == pygame.K_f:
                #e=pygame.VIDEORESIZE
                #pygame.event.post(e)
                
                fNotPressed=False
                print("K_f, full:",fullScr)
                if(fullScr):
                    #screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)
                    print("K_f, full:",fullScr)
                    resize(screenSize,pygame.RESIZABLE,screen)
                    print("K_f, fullT:",fullScr)
                    
                else:
                    #screen = pygame.display.set_mode(monitorSize, pygame.FULLSCREEN)
                    #screen = pygame.display.set_mode((monitorSize),pygame.RESIZABLE)
                    resize(monitorSize,pygame.FULLSCREEN,screen)
                    print("K_f, fullF:",fullScr)
                
               
                fullScr= not fullScr
                   
        #print("loop, fNotPressed:",fNotPressed)
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButt=event.button
            rObjekt1.destX=mouseXY[0]
            rObjekt1.destY=mouseXY[1]
        """
        if pygame.mouse.get_pressed()[0]:
            #mouseButt=event.button
            rObjekt1.destX=mouseXY[0]
            rObjekt1.destY=mouseXY[1]
        if event.type == pygame.VIDEORESIZE:
            if(fNotPressed):
                print(".VIDEORESIZE, fNotPressed:",fNotPressed)
                screenSize=event.w,event.h
                #screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
                resize(screenSize,pygame.RESIZABLE,screen)
            fNotPressed=True
                
    else: mouseButt=0;
    


    rObjekt1.moveOneStep();


    screen.fill(black)
    #screen.blit(ball, ballrect)
    #drawBackgroundNet(screen)
    drawBackgroundNet(
        screen,
        info={
            "x":playerX,
            "y":playerY,
            "distance":50
            })
    for o in rooms[0].objList:
        pygame.draw.circle(screen, blue, o.place(), o.radius, 1)
    """
    pygame.draw.circle(screen, blue, rooms[0].objList[0].place(), rooms[0].objList[0].radius, 1)
    pygame.draw.circle(screen, blue, rooms[0].objList[1].place(), rooms[0].objList[1].radius, 1)
    pygame.draw.circle(screen, blue, rooms[0].objList[2].place(), rooms[0].objList[2].radius, 1)
    pygame.draw.circle(screen, blue, rooms[0].objList[3].place(), rooms[0].objList[3].radius, 1)
    pygame.draw.circle(screen, blue, rooms[0].objList[4].place(), rooms[0].objList[4].radius, 1)
    """
    pygame.draw.rect(screen, (0,255,0), (10,10,20,10))
    pygame.display.flip()
    

    for i, o in enumerate(rooms[0].objList):    #detekcija sudara igrača s kružnim objektima
        if i>0:
            if udaljenostTocaka(o.x,o.y,po.x,po.y)<o.radius+po.radius:
                #print("njam",i)
                rooms[0].objList.pop(i)
                pogodak.play()
        else:
            po=o
"""
izbacio udaljenostTocaka()
automatizirao ispis objekata
napravio detekciju sudara
napravio reset objekata
    inputObj
    tipka za reset
dodao zvuk
    učitao pozadinu i udarac
    upotrijebio udarac
Dodao brojanje u glavnu petlju i varijablu fps
dodao stvaranje novih objekata nedaleko od igrača
funkcija za crtanje mreže drawBackgroundNet
"""
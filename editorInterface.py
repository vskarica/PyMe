import sys, pygame,os
import random
import json
import editorFunkcije
from editorGlobal import *

#from ctypes import windll, Structure, c_long, byref
import win32api
#import TKmultiple Pr1.update()
pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' %(varijable.koordinateProzoraX, varijable.koordinateProzoraY)
varijable.screen = pygame.display.set_mode(varijable.screenSize, pygame.RESIZABLE)

varijable.screenDebug.set_alpha(128)

pygame.font.init()

#Izvršava pojedine funkcije objekata vezane uz pygame evente
def izvrsiEditorEvente(event):
    #za svaki unos funkcije za događaj dotičnog tipa ... izvrši je
    #for ObjIme in varijable.eventsQuery[event.type]:
    brojac=0
    
    while (brojac<len(varijable.eventsQuery[event.type])):
        ObjIme=list(varijable.eventsQuery[event.type])[brojac]#varijable.eventsQuery[event.type][brojac]

        varijable.eventsQuery[event.type][ObjIme](event)
        if event.type==5:
            a=0
        if event.type==4:
            a=0
        brojac+=1

#zodavanje pomaknutog zumiranog elementa na površinu
def addEllToSurf(surf1,surf2,shift=(0,0),zoom=1):
    surf2WH=surf2.get_size()
    #varijable.GameZoom=zoom
    shift=(
        int(round(shift[0]*zoom)),
        int(round(shift[1]*zoom))
        )

    surf1.blit(
        pygame.transform.scale(
            surf2,
            (
                int(round(surf2WH[0]*zoom)),
                int(round(surf2WH[1]*zoom))
            )
        ),
        shift
    )
    #print(surf2.get_size())
def crtanje(lista,scr):
    for item in lista:
        if type(item) is list:
            crtanje(item,scr)
        else:
            item.nacrtajMe(scr)

"""
class sucelje:
    def __init__(self):
        self.PrikaziDesno=True
        self.x=10
        self.y=10
    
    def nacrtajMe(self): 
        pass


class nivo:
    def __init__(self,ime):
        self.ime=ime
        self.konteinter=[]

class sloj:
    def __init__(self,ime,x=0,y=0):
        self.ime=ime
        self.x=x
        self.y=y
        self.konteinter=[]
"""
class eventInterakcija:
    def __init__(self,ime=""):
        if ime=="":
            self.ime= str(random.getrandbits(128))
            print("nasumično ime:",self.ime)
        else:
            self.ime=ime        

        varijable.eventsQuery[pygame.QUIT           ].update ({self.ime:self.QUIT           })
        varijable.eventsQuery[pygame.KEYDOWN        ].update ({self.ime:self.KEYDOWN        })
        varijable.eventsQuery[pygame.ACTIVEEVENT    ].update ({self.ime:self.ACTIVEEVENT    })
        varijable.eventsQuery[pygame.KEYUP          ].update ({self.ime:self.KEYUP          })
        varijable.eventsQuery[pygame.MOUSEMOTION    ].update ({self.ime:self.MOUSEMOTION    })
        varijable.eventsQuery[pygame.MOUSEBUTTONUP  ].update ({self.ime:self.MOUSEBUTTONUP  })
        varijable.eventsQuery[pygame.MOUSEBUTTONDOWN].update ({self.ime:self.MOUSEBUTTONDOWN})
        varijable.eventsQuery[pygame.JOYAXISMOTION  ].update ({self.ime:self.JOYAXISMOTION  })
        varijable.eventsQuery[pygame.JOYBALLMOTION  ].update ({self.ime:self.JOYBALLMOTION  })
        varijable.eventsQuery[pygame.JOYHATMOTION   ].update ({self.ime:self.JOYHATMOTION   })
        varijable.eventsQuery[pygame.JOYBUTTONUP    ].update ({self.ime:self.JOYBUTTONUP    })
        varijable.eventsQuery[pygame.JOYBUTTONDOWN  ].update ({self.ime:self.JOYBUTTONDOWN  })
        varijable.eventsQuery[pygame.VIDEORESIZE    ].update ({self.ime:self.VIDEORESIZE    })
        varijable.eventsQuery[pygame.VIDEOEXPOSE    ].update ({self.ime:self.VIDEOEXPOSE    })
        varijable.eventsQuery[pygame.USEREVENT      ].update ({self.ime:self.USEREVENT      })

    def QUIT(self,ev):pass
    def ACTIVEEVENT(self,ev):pass
    def KEYDOWN(self,ev):pass
    def KEYUP(self,ev):pass
    def MOUSEMOTION(self,ev):pass
    def MOUSEBUTTONUP(self,ev):pass
    def MOUSEBUTTONDOWN(self,ev):pass
    def JOYAXISMOTION(self,ev):pass
    def JOYBALLMOTION(self,ev):pass
    def JOYHATMOTION(self,ev):pass
    def JOYBUTTONUP(self,ev):pass
    def JOYBUTTONDOWN(self,ev):pass
    def VIDEORESIZE(self,ev):pass
    def VIDEOEXPOSE(self,ev):pass
    def USEREVENT(self,ev):pass

class objekt():
    djcjeKlase=[]
    def __init__(self,ime,x=0,y=0,w=10,h=10,PutDoSlike="media/NemaSlike.png",grupa=varijable.GrupaIgra,prozirnost=255):
        self.surf = pygame.image.load(PutDoSlike).convert()
        self.surf = pygame.transform.scale(self.surf,(w,h))
        self.rect = self.surf.get_rect()
        self.ime=ime
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.slika =pygame.image.load("media/intro_ball.gif")
        self.scrD=varijable.screenDebug
        self.lista=grupa
        self.prozirnost = prozirnost
        
    def nacrtajMe(self,screen):
        #pygame.draw.rect(screen, (0,0,255), (self.x,self.y,self.w,self.h))
        #self.surf.fill((255,0,0))#, rect=None, special_flags=0)
        self.surf=pygame.transform.scale(self.surf, (self.w,self.h))
        self.surf.set_alpha(self.prozirnost)
        screen.blit(self.surf, (self.x,self.y))#,self.w,self.h


        
    def ucitajSliku(self,datoteka):
        self.slika = pygame.image.load(datoteka)

        

        #print(self.x+10,self.y+10,self.w,self.h)
    @classmethod
    def GetSubclasses(cls):
        #objekt.djcjeKlase=objekt.__subclasses__()
        return cls.__subclasses__()
class objektE(objekt):
    def __init__(self,ime,x=0,y=0,w=10,h=10,PutDoSlike="NemaSlike.png",grupa="GrupaSucelje",prozirnost=255):
        objekt.__init__(self,ime,x,y,w,h,PutDoSlike,grupa,prozirnost)
        eventInterakcija.__init__(self,ime)
        
        self.scr=varijable.screenEditor
        self.lista=grupa #varijable.GrupaEditor
        self.lista.append(self)
class objektG(objekt):
    def __init__(self,ime,x=0,y=0,w=10,h=10,PutDoSlike="NemaSlike.png",grupa="GrupaIgra",prozirnost=255):
        objekt.__init__(self,ime,x,y,w,h,PutDoSlike,grupa,prozirnost)
        eventInterakcija.__init__(self,ime)

        self.oznacen=False
        self.scr=varijable.screenGame
        self.lista=varijable.GrupaIgra#varijable[grupa]#grupa #varijable.GrupaIgra
        self.lista.append(self)
        #print("--",varijable.GrupaIgra)

        self.listaSave=varijable.GrupaIgraSave
        self.listaSave.append([ime,x,y,w,h,PutDoSlike,type(self).__name__])

        objektG.djcjeKlase.append(self.ime)

    def nacrtajMe(self,screen):
         objekt.nacrtajMe(self,screen)
         if self.ime in varijable.GrupaOznacenihObjekata:
             pygame.draw.rect(self.scr, (0, 255, 0), (self.x, self.y, self.w, self.h), 3)




class gumb(objektE,eventInterakcija):
    pass

class gumbZoomIn(objektE,eventInterakcija):
    def MOUSEBUTTONDOWN(self,ev):
        #pygame.MOUSEBUTTONDOWN
        inp=pygame.mouse
        mx,my=inp.get_pos()
        
        self.xzoom=round(self.x*varijable.EditorZoom)
        self.yzoom=round(self.y*varijable.EditorZoom)
        self.wzoom=round(self.w*varijable.EditorZoom)
        self.hzoom=round(self.h*varijable.EditorZoom)

        if(mx>=self.xzoom and mx<=self.xzoom+self.wzoom and my>=self.yzoom and my<=self.yzoom+self.hzoom):
            gameZoomIn()


class gumbZoomOut(objektE,eventInterakcija):
    def MOUSEBUTTONDOWN(self,ev):
        inp=pygame.mouse
        mx,my=inp.get_pos()
        
        self.xzoom=round(self.x*varijable.EditorZoom)
        self.yzoom=round(self.y*varijable.EditorZoom)
        self.wzoom=round(self.w*varijable.EditorZoom)
        self.hzoom=round(self.h*varijable.EditorZoom)

        if(mx>=self.xzoom and mx<=self.xzoom+self.wzoom and my>=self.yzoom and my<=self.yzoom+self.hzoom):
            gameZoomOut()

class gumbZoomFit(objektE,eventInterakcija):
    def MOUSEBUTTONDOWN(self,ev):
        inp=pygame.mouse
        mx,my=inp.get_pos()
        
        self.xzoom=round(self.x*varijable.EditorZoom)
        self.yzoom=round(self.y*varijable.EditorZoom)
        self.wzoom=round(self.w*varijable.EditorZoom)
        self.hzoom=round(self.h*varijable.EditorZoom)

        if(mx>=self.xzoom and mx<=self.xzoom+self.wzoom and my>=self.yzoom and my<=self.yzoom+self.hzoom):
            gameZoomFit()


class gumbUpisivanjeIgre (objektE,eventInterakcija):
    def MOUSEBUTTONDOWN(self,ev):
        inp=pygame.mouse
        mx,my=inp.get_pos()
        
        self.xzoom=round(self.x*varijable.EditorZoom)
        self.yzoom=round(self.y*varijable.EditorZoom)
        self.wzoom=round(self.w*varijable.EditorZoom)
        self.hzoom=round(self.h*varijable.EditorZoom)

        if(mx>=self.xzoom and mx<=self.xzoom+self.wzoom and my>=self.yzoom and my<=self.yzoom+self.hzoom):
            with open('objektiIgre.txt', 'w') as filehandle:
                json.dump(varijable.GrupaIgraSave, filehandle)
            print ("OVo je test upisivanja")

class gumbUcitavanjeIgre (objektE,eventInterakcija):
    def MOUSEBUTTONDOWN(self,ev):
        inp=pygame.mouse
        mx,my=inp.get_pos()
        
        self.xzoom=round(self.x*varijable.EditorZoom)
        self.yzoom=round(self.y*varijable.EditorZoom)
        self.wzoom=round(self.w*varijable.EditorZoom)
        self.hzoom=round(self.h*varijable.EditorZoom)

        if(mx>=self.xzoom and mx<=self.xzoom+self.wzoom and my>=self.yzoom and my<=self.yzoom+self.hzoom):
            igra_ucitaj()

class suceljeDragBox (objektE,eventInterakcija):
    kliknut=False
    def MOUSEBUTTONUP(self,ev):
        self.kliknut=False
        self.x=self.y=self.w=self.h=0
    def MOUSEBUTTONDOWN(self,ev):
        self.kliknut=True
        #self.x,self.y=ev.pos
        self.x1,self.y1=ev.pos
    def MOUSEMOTION(self,ev):
        if self.kliknut:
            x1=self.x1      #prve (inicijalna) koordinate miša
            y1=self.y1
            x2,y2=ev.pos    #druge (trenutna) koordinate miša

            #self.w=x-self.x
            #self.h=y-self.y
            self.w=x2-x1
            self.h=y2-y1

            if(self.w<0):
                self.x=x2
            else:
                self.x=x1
            self.w=abs(self.w)
            
            if(self.h<0):
                self.y=y2
            else:
                self.y=y1
            self.h=abs(self.h)


            #print(self.w,self.h)
            
    #def nacrtajMe(self,screen):
        #pygame.draw.rect(screen, (255,255,255,200), (self.x,self.y,self.w,self.h))
        #s=pygame.Surface ((self.w,self.H))
        #s.set_alpha(200)
        #screen.blit(self.surf, (self.x,self.y,self.w,self.h))
        """
        inp=pygame.mouse
        mx,my=inp.get_pos()
        
        self.xzoom=round(self.x*varijable.EditorZoom)
        self.yzoom=round(self.y*varijable.EditorZoom)
        self.wzoom=round(self.w*varijable.EditorZoom)
        self.hzoom=round(self.h*varijable.EditorZoom)

        if(mx>=self.xzoom and mx<=self.xzoom+self.wzoom and my>=self.yzoom and my<=self.yzoom+self.hzoom):
            editorFunkcije.ucitajIgru("asdfa")
        """
class objekt0(eventInterakcija):
    def QUIT(self,ev):
        varijable.MainLoop=False
    #def ACTIVEEVENT(self,ev):pass
    def KEYDOWN(self,ev):
        if ev.key == pygame.K_ESCAPE:
            varijable.MainLoop=False
    #def KEYUP(self,ev):pass
    def MOUSEMOTION(self,ev):
        inp=pygame.mouse
        mx,my=inp.get_pos()
        ex, ey = win32api.GetCursorPos()
        pgwX=ex-mx
        pgwY=ey-my
        if(varijable.koordinateProzoraX!=pgwX or varijable.koordinateProzoraY!=pgwX):
            #global sucelja
            if(len(varijable.sucelja)):
                #pass
                varijable.koordinateProzoraX=pgwX
                varijable.koordinateProzoraY=pgwY
                varijable.sucelja[0].geometry('%dx%d+%d+%d' % (200, 400, varijable.sucelja[0].getX(), varijable.sucelja[0].getY()))#varijable.koordinateProzoraX, varijable.koordinateProzoraY
                print(varijable.sucelja[0].getX(), varijable.sucelja[0].getY())
        
    #def MOUSEBUTTONUP(self,ev):pass
    #def MOUSEBUTTONDOWN(self,ev):pass
    #def JOYAXISMOTION(self,ev):pass
    #def JOYBALLMOTION(self,ev):pass
    #def JOYHATMOTION(self,ev):pass
    #def JOYBUTTONUP(self,ev):pass
    #def JOYBUTTONDOWN(self,ev):pass
    def VIDEORESIZE(self,ev):
        varijable.screenSize=ev.size
        #arijable.screen = pygame.display.set_mode(varijable.screenSize, pygame.RESIZABLE)
        varijable.screenReSized=True
        """
        screenSize=ev.size
        print(screenSize)

        #screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
        screenEditor = pygame.transform.scale(screenEditor, screenSize)
        screenDebug = pygame.transform.scale(screenDebug, screenSize)

        screen.fill((255,0,0,0))
        screenGame.fill((0,0,0,0))
        screenEditor.fill((0,0,200,0))
        #screenDebug.set_alpha(255)
        """
    #def VIDEOEXPOSE(self,ev):pass
    #def USEREVENT(self,ev):pass    

class objektUIgri(objektG,eventInterakcija):
    def MOUSEBUTTONDOWN(self,ev):
        #pygame.MOUSEBUTTONDOWN
        #inp=pygame.mouse
        mx,my=pygame.mouse.get_pos()
        
        self.xzoom=round(self.x*varijable.GameZoom)
        self.yzoom=round(self.y*varijable.GameZoom)
        self.wzoom=round(self.w*varijable.GameZoom)
        self.hzoom=round(self.h*varijable.GameZoom)

        if(mx>=self.xzoom and mx<=self.xzoom+self.wzoom and my>=self.yzoom and my<=self.yzoom+self.hzoom):
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                varijable.GrupaOznacenihObjekata.append(self.ime)
            else:
                varijable.GrupaOznacenihObjekata=[self.ime]
            #
            
            print(self.prozirnost)
            #print("kliknuo si", self.ime,self.scr,self.scrD,varijable.screenGame)

        #mx,my=(0,0)



"""
1. zum gumbi (miš i tipkovnica)
1.1. kretanje kroz mapu (tipke)
2. umetanje objekta (miš)
2.1 odabir objekta za umetanje
2.2 ometanje objekta za uređivanje
2.2 lista umetnutih objekata

3.1 biranje nivoa
3.2 biranje sloja
4. selidba sučelja

5. definicija veličine prozora (1080*640)

+- S
<>AV
nivoi A V (x/xx)
objekti A V (x/xx)
sloj A V (x/xx)
umetnuti A V (x/xx)

"""

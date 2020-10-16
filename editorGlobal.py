import sys, pygame, json, editorInterface

class varijable:
    events=[
        pygame.QUIT,
        pygame.ACTIVEEVENT,
        pygame.KEYDOWN,
        pygame.KEYUP,
        pygame.MOUSEMOTION,
        pygame.MOUSEBUTTONUP,
        pygame.MOUSEBUTTONDOWN,
        pygame.JOYAXISMOTION,
        pygame.JOYBALLMOTION,
        pygame.JOYHATMOTION,
        pygame.JOYBUTTONUP,
        pygame.JOYBUTTONDOWN,
        pygame.VIDEORESIZE,
        pygame.VIDEOEXPOSE,
        pygame.USEREVENT
    ]
    eventsQuery={
        pygame.QUIT:{},
        pygame.ACTIVEEVENT:{},
        pygame.KEYDOWN:{},
        pygame.KEYUP:{},
        pygame.MOUSEMOTION:{},
        pygame.MOUSEBUTTONUP:{},
        pygame.MOUSEBUTTONDOWN:{},
        pygame.JOYAXISMOTION:{},
        pygame.JOYBALLMOTION:{},
        pygame.JOYHATMOTION:{},
        pygame.JOYBUTTONUP:{},
        pygame.JOYBUTTONDOWN:{},
        pygame.VIDEORESIZE:{},
        pygame.VIDEOEXPOSE:{},
        pygame.USEREVENT:{}
    }
    #screenGame=None
    EditorZoom=1
    GameZoom=1
    GamePan =(0,0)
    screenSize=1200,700
    screenReSized=False
    screenGameSize=1080,640
    screenGameCurentSize=screenGameSize
    MainLoop=True
    GrupaEditor=[]
    koordinateProzoraX=50
    koordinateProzoraY=50
    sucelja=[]
    sloj0=[]
    sloj1=[]
    sloj2=[]
    sloj3=[]
    sloj4=[]
    sloj5=[]
    sloj6=[]
    sloj7=[]
    sloj8=[]
    sloj9=[]
    GrupaIgra=[]#[sloj0,sloj1,sloj2,sloj3,sloj4,sloj5,sloj6,sloj7,sloj8,sloj9]
    GrupaIgraSave=[]
    #GrupaIgra.append()
    GrupaOznacenihObjekata=[]
    #"""
    screenGame = pygame.Surface (screenGameSize)
    screenEditor = pygame.Surface (screenSize)
    screenDebug = pygame.Surface (screenSize)
    #screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
    #"""

def gameZoomIn():
    varijable.GameZoom*=(10/9)

def gameZoomOut():
    varijable.GameZoom *=0.9

def gameZoomFit():
    ScrWH =ScrW, ScrH = varijable.screen.get_size()#varijable.screenEditor.get_size()
    GamWH =GamW, GamH = varijable.screenGame.get_size()
    
    RW= ScrW/GamW
    RH= ScrH/GamH
    if RW>RH:   #ako je omer širina veći
        #izjednači širinu
        o=RH
    else:       #ako je omer visina veći
        #izjednači visinu
        o=RW
    NH=GamH*o
    NW=GamW*o
    varijable.GameZoom=o

def igra_ucitaj():
    ucitajIgru("asdfa")
def igra_sacuvaj():
    pass

def ucitajIgru(PutDoIgre):  #PutDoIgre -put do glavne .py datoteke
    #grupa=editorInterface.varijable.GrupaIgra
    #objektUIgri1  =editorInterface.objektUIgri("objektUIgri1",100,100,100,100,"media/SuceljePlus.png",editorInterface.varijable.sloj9)
    #objektUIgri3  =editorInterface.objektUIgri("objektUIgri3",150,150,100,100,"media/SuceljePlus.png",editorInterface.varijable.sloj5)
    #objektUIgri2  =editorInterface.objektUIgri("objektUIgri2",200,200,100,100,"media/SuceljePlus.png",editorInterface.varijable.sloj0)
    varijable.GrupaIgraSave=[]
    varijable.GrupaIgra=[]

    with open('objektiIgre.txt', 'r') as filehandle:
        listaUcitanih = json.load(filehandle)
    for Podaci in listaUcitanih:
        editorInterface.objektUIgri(
            Podaci[0],
            Podaci[1],
            Podaci[2],
            Podaci[3],
            Podaci[4],
            Podaci[5])
    #print(varijable.GrupaIgraSave)
    #print ("OVo je test učitavanja")
micanje=False
tkx=0
tky=0
def suceljeGumb1klik(event):
    global micanje,tkx,tky
    micanje=True
    tkx=event.x
    tky=event.y

    #print(micanje)
def suceljeGumb1move(event):
    global micanje,tkx,tky
    if(micanje):
        event.widget.geometry("200x400+"+str(event.x_root-tkx)+"+"+str(event.y_root-tky))

def suceljeGumb1release(event):
    global micanje,tkx,tky
    micanje=False
    varijable.sucelja[0].setX(event.x_root-tkx)
    varijable.sucelja[0].setY(event.y_root-tky)
    
    #print(micanje)

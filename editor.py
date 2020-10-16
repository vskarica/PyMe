import sys, pygame,os
"""
import time
time.sleep(2)
#set where the display will move to
x=500
y=500
os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d' %(x,y)"""

from editorInterface import *
from editorFunkcije import *
from editorGlobal import *
#import TKmultiple
import TKmodul

#from win32gui import GetWindowText, GetForegroundWindow


ucitajEditor()
#ucitajIgru("prvaigra.py")
programIcon = pygame.image.load("media/missle.png")
pygame.display.set_icon(programIcon)


pygame.draw.rect(varijable.screenGame, (0, 50, 50), (50, 50, 60, 60), 5)  # width = 3
#varijable.MainLoop=True
while varijable.MainLoop:
    if varijable.screenReSized:
        os.environ['SDL_VIDEO_WINDOW_POS'] = '50,50'
        varijable.screenDebug  = pygame.Surface (varijable.screenSize)
        varijable.screenEditor = pygame.Surface (varijable.screenSize)
        varijable.screenDebug.set_alpha(128)
        varijable.screenEditor.set_alpha(128)
        varijable.screenReSized=False
        #pass
    
    varijable.screen.fill((0,0,255,0))
    varijable.screenGame.fill((0,0,0,0))
    varijable.screenEditor.fill((0,0,200,0))
    varijable.screenDebug.fill((0,0,200,0))

    for event in pygame.event.get():
        izvrsiEditorEvente(event)


    #crta objekte iz grupe sučelje i grupe igra
    crtanje(varijable.GrupaEditor,varijable.screenEditor)
    crtanje(varijable.GrupaIgra,varijable.screenGame)
    


    #screenEditor.blit(screenGame,(1,1))
    addEllToSurf(varijable.screen,varijable.screenGame,(0,0),varijable.GameZoom)
    addEllToSurf(varijable.screen,varijable.screenEditor,(0,0),varijable.EditorZoom)
    #screenEditor.set_alpha(100)
    #varijable.screen.blit(varijable.screenEditor,(0,0))
    ####varijable.screen.blit(varijable.screenDebug,(0,0))
    
    
    pygame.display.flip()
    try:
        varijable.sucelja[0].update()
    except:
        pass
        #print("nema prozora")


    """
    plan
    osposobiti dragbox
        učiniti prozirnim (dodati prozirnost u "objekt" klasu)
        
    -omogućiti čitanje objekata iz baze i pisanje u bazu
    raditri na na slojevima igre i sučelja
    objektificirati

    osposobiti navigaciju sučelja
    osposobiti editiranje objekata u igri
"""
    
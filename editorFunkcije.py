import sys, pygame, json
from editorGlobal import *
import editorInterface

def ucitajEditor():
    grupa=varijable.GrupaEditor
    ostaliEventiEditoraObjekt = editorInterface.objekt0("OstaliEventiEditoraObjekt")
    """
    zoomIn   =editorInterface.gumbZoomIn("zoomIn",300,300,50,50,"media/SuceljePlus.png",grupa)
    zoomOut  =editorInterface.gumbZoomOut("zoomOut",350,300,50,50,"media/SuceljeMinus.png",grupa)
    zoomFit  =editorInterface.gumbZoomFit("zoomFit",400,300,50,50,"media/SuceljeFit.png",grupa)
    panUp    =editorInterface.gumb("panUp",325,350,50,50,"media/SuceljeGore.png",grupa)
    panDown  =editorInterface.gumb("panDown",325,450,50,50,"media/SuceljeDolje.png",grupa)
    panLeft  =editorInterface.gumb("panLeft",300,400,50,50,"media/SuceljeLijevo.png",grupa)
    panRight =editorInterface.gumb("panRight",350,400,50,50,"media/SuceljeDesno.png",grupa)
    SNext    =editorInterface.gumb("SNext",300,500,50,50,"media/SuceljeGore.png",grupa)
    SPrevious=editorInterface.gumb("SPrevious",350,500,50,50,"media/SuceljeDolje.png",grupa)
    ucitajIgru =editorInterface.gumbUpisivanjeIgre("ucitajIgru",300,550,50,50,"media/SuceljePlus.png",grupa)
    ucitajIgru =editorInterface.gumbUcitavanjeIgre  ("ucitajIgru",  350,550,50,50,  "media/SuceljeMinus.png", grupa)
"""
    dragBox=    editorInterface.suceljeDragBox      ("dragBox",     0,0,0,0,        "media/NemaSlike.png",    grupa, 50)
    



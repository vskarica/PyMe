import tkinter
from tkinter.ttk import *
if __name__ == "__main__":
    def gameZoomIn():
        pass
    def gameZoomOut():
        pass
    def gameZoomFit():
        pass
    def igra_ucitaj():
        pass
    def igra_sacuvaj():
        pass
else:
    from editorGlobal import *
svojstva={
    #'-type':'splash',
    '-alpha', 0.6,
    "-topmost", True
}
class tkinterTk(tkinter.Tk):
    def __init__(self):
        self.x=0
        self.y=0
        super().__init__()
    def getX(self):
        return self.x+varijable.koordinateProzoraX
    def getY(self):
        return self.y+varijable.koordinateProzoraX
    def setX(self,vrijednost):
        self.x=vrijednost-varijable.koordinateProzoraX
    def setY(self,vrijednost):
        self.y=vrijednost-varijable.koordinateProzoraY

varijable.sucelja=[]
varijable.sucelja.append(tkinterTk())
#varijable.sucelja.append(tkinter.Tk())
#varijable.sucelja[0].wm_attributes('-type', 'splash')
trTk=varijable.sucelja[0]
trTk.title("editor")
trTk.x=100
trTk.y=200
trTk.iconbitmap("media/Custom-Icon-Design-Mono-Business-2-Coffee.ico")
trTk.attributes('-alpha', 0.6)
trTk.attributes("-topmost", True)
#trTk.attributes(**svojstva)

trTk.geometry('%dx%d+%d+%d' % (200, 400, trTk.getX(), trTk.getY()))#varijable.koordinateProzoraX, varijable.koordinateProzoraY
trTk.overrideredirect(True)
trTk.bind("<Button-1>",suceljeGumb1klik)
trTk.bind("<B1-Motion>",suceljeGumb1move)
trTk.bind("<ButtonRelease-1>",suceljeGumb1release)


tkinter.Button(trTk,text="+",command=gameZoomIn).grid(row=0,column=0)
tkinter.Button(trTk,text="-",command=gameZoomOut).grid(row=0,column=1)
tkinter.Button(trTk,text="Fit",command=gameZoomFit).grid(row=0,column=2)
tkinter.Button(trTk,text="Učitaj",command=igra_ucitaj).grid(row=1,column=0, columnspan=3)
tkinter.Button(trTk,text="Sačuvaj",command=igra_sacuvaj).grid(row=1,column=3)
tkinter.Button(trTk,text="t").grid(row=2,column=0)

tkinter.Button(trTk,text="t").grid(row=3,column=0)
tkinter.Button(trTk,text="t").grid(row=4,column=0)
def mojtest():
    trTk.geometry('%dx%d+%d+%d' % (200, 400, 100,100))
tkinter.Button(trTk,text="t",command=mojtest).grid(row=5,column=0)



if __name__ == "__main__":tkinter.mainloop()



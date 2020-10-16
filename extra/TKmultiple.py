from tkinter import *
#from PIL import ImageTK, Image

Pr1=Tk()
#Pr2=Tk()
#Pr3=Tk()
Pr1.geometry("200x200")
#Pr2.geometry("300x300")
Pr1.title("Više prozora")
#Pr2.title("+1")
#Pr3.title("+2")
#Pr2.withdraw()
Pr1.iconbitmap("Custom-Icon-Design-Mono-Business-2-Coffee.ico")

def noviPr():
    global my_img
    top=Toplevel()
    top.geometry("200x200")
    top.title("Novi prozor")
    top.iconbitmap("Custom-Icon-Design-Mono-Business-2-Coffee.ico")
    btn=Button(top,text="zatvori", command=top.destroy).pack()
def sakrij(pr):
    pr.withdraw()
def otkrij(pr):
    pr.deiconify()

btn=Button(Pr1,text="Otvori novi prozor", command=noviPr).pack()
btn2=Button(Pr1,text="Sokrij", command=lambda:sakrij(Pr2)).pack()
btn3=Button(Pr1,text="Otkrij", command=lambda:otkrij(Pr2)).pack()

mainloop()
    
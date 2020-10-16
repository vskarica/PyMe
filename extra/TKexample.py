import tkinter
from tkinter.ttk import *

prozor=tkinter.Tk()
prozor.title("Naslov prozora")
prozor.geometry("400x800")
prozor.resizable(0,0)

""" Okviri
#okvir1=tkinter.LabelFrame(prozor,text="asdfsd",padx=50,pady=50).pack(padx=5,pady=5)
#okvir2=tkinter.LabelFrame(prozor,text="gsdhsfhsdfzh",padx=50,pady=50).pack(padx=5,pady=5,side="bottom")
okvir1=tkinter.Frame(prozor).pack()
okvir2=tkinter.Frame(prozor).pack(side="bottom")

bot1=tkinter.Button(okvir1,text="B1",fg="red").pack()
bot2=tkinter.Button(okvir1,text="B2",fg="green").pack()
bot3=tkinter.Button(okvir2,text="B3",fg="purple").pack(side="left")
bot3=tkinter.Button(okvir2,text="B4",fg="orange").pack(side="left")
"""

""" Cijela šitina i visina
tkinter.Label(prozor,text="malo teksta 1",bg="purple",fg="white").pack()
tkinter.Label(prozor,text="malo teksta 2",bg="green",fg="white").pack(fill="x")
tkinter.Label(prozor,text="malo teksta 3",bg="black",fg="white").pack(side="left",fill="y")
"""

#""" Gumbi miša
tkinter.Label(prozor,text="Tekst 1").grid(row=0)
tkinter.Entry(prozor).grid(row=0,column=1)
tkinter.Label(prozor,text="Tekst 2").grid(row=1)
tkinter.Entry(prozor).grid(row=1,column=1)
tkinter.Checkbutton(prozor,text="login").grid(columnspan=2)

#def say_hi():
def say_hi(event):
    tkinter.Label(prozor,text="Oj!").grid()
def say_hii():
    tkinter.Label(prozor,text="Oj!").grid()

#tkinter.Button(prozor,text="Bok!",command=say_hi).grid()
bot=tkinter.Button(prozor,text="Bok!")
bot.bind("<Button-1>",say_hi)
bot.grid()
#bot.propagate()
def b1(event):
    prozor.title("B1")
def b2(event):
    prozor.title("B2")
def b3(event):
    prozor.title("B3")
prozor.bind("<Button-1>",b1)
prozor.bind("<Button-2>",b2)
prozor.bind("<Button-3>",b3)

icon=tkinter.PhotoImage(file="NemaSlike.png")
l1=tkinter.Label(bot,image=icon)
l1.grid()
l2=tkinter.Label(bot,image=icon).grid()
l1.propagate()
#"""

#""" Combo
combo=Combobox(prozor)
combo["values"]=(1,2,3,4,5,"asdf")
combo.bind("<Button-1>",b1)
combo.current(3)
combo.grid()
#"""

# Adding widgets to the root window 
Label(prozor, text = 'GeeksforGeeks', font =( 
  'Verdana', 15)).grid() 
  
 
# here, image option is used to 
# set image on button 
Button(prozor, text = 'Click Me !', image = icon,command=say_hii).grid() 

if __name__ == "__main__":tkinter.mainloop()
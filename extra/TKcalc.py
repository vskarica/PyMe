from tkinter import *

prozor=Tk()
prozor.title("TK Calc")
prozor.geometry("312x324")
prozor.resizable(0,0)

def btn_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression=""
    input_text.set(expression)
def btn_equal():
    global expression
    resault=str(eval(expression))
    input_text.set(resault)
    expression=""

expression=""
input_text=StringVar()

input_frame=Frame(prozor,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black")
input_frame.pack(side="top")

input_field=Entry(input_frame,font=("areal",18,"bold"),textvariable=input_text, width=50,bg="#fff", bd=0,justify="center")
input_field.grid()
input_field.pack(ipady=20)

btns_frame=Frame(prozor,width=312, height=272.5, bg="red")
btns_frame.pack()

clear   =Button(btns_frame,text="C", width=32, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_clear()).grid(columnspan=3)
divide  =Button(btns_frame,text="/", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("/")).grid(row=0,column=3)

b7  =Button(btns_frame,text="7", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("7")).grid(row=1,column=0)
b8  =Button(btns_frame,text="8", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("8")).grid(row=1,column=1)
b9  =Button(btns_frame,text="9", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("9")).grid(row=1,column=2)
bM  =Button(btns_frame,text="*", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("*")).grid(row=1,column=3)

b4  =Button(btns_frame,text="4", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("4")).grid(row=2,column=0)
b5  =Button(btns_frame,text="5", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("5")).grid(row=2,column=1)
b6  =Button(btns_frame,text="6", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("6")).grid(row=2,column=2)
bO  =Button(btns_frame,text="-", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("-")).grid(row=2,column=3)

b1  =Button(btns_frame,text="1", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("1")).grid(row=3,column=0)
b2  =Button(btns_frame,text="2", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("2")).grid(row=3,column=1)
b3  =Button(btns_frame,text="3", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("3")).grid(row=3,column=2)
bZ  =Button(btns_frame,text="+", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("+")).grid(row=3,column=3)

b0  =Button(btns_frame,text="0", width=21, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click("0")).grid(row=4,columnspan=2)
bT  =Button(btns_frame,text=".", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_click(".")).grid(row=4,column=2)
bJ  =Button(btns_frame,text="=", width=10, height=3,bd=0,bg="#eee",cursor="hand2",highlightthickness=1,command=lambda: btn_equal()).grid(row=4,column=3)




prozor.mainloop()
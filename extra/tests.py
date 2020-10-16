from myGameClasees import *
import math
import random
import pygame

a = v2d((5, 6))
b = v2d((5, 7))
c = v2d()
c = a+b
d=v2d((0, 1))
print("d.len:", d.len(), "d.(90):", d.rotate(radians(90)))
print("cos(90):", round(cos(radians(90))))
print((5**2)*(3**2))
print((5*3)**2)
print(tan(radians(10)))

o=[]

for i in range(10):
    xy=random.randint(1, 10),random.randint(1, 10)
    oo=GameObject(xy)
    o.append(oo)
    #print(o[i].gsxy(),(o[i].id),GameObject.id)
    if i%3==0: del oo

print(o)

a=["a","s","d","f","g"]
b=["b","š","dž","g","h"]
for i,(c,d) in enumerate(zip(a,b), start=1):
    print(f'{i}. poslje {c} dođe {d}')

#nasljedsvo i deklaracija stringom
class aa:
    myvar=0
    def mymet(self,x):
        print(x)
    def __init__(self,x):
        print("iniciran sam s:",x)

class aa2(aa):
    mymyvar=1

def myfun():

    a1=eval("aa2")(";D")
    print("nasljedstrvo:",a1.myvar,a1.mymyvar)
    a1.mymet("XXX")

myfun()

aaa=aa()

var1="dinamickiAtribut"
var2="vrijednostDinamickogAtributa"

setattr(aaa,var1,var2)
print(getattr(aaa,var1))


bb={
    "b":"bebe",
    "c":{"c":"cece"}
}
print(bb["c"]["c"])
myOb=GameObject((5,5),2,2)
myRect=pygame.Rect(myOb)
print(myRect.collidepoint(2,2))
print(myRect.collidepoint(5,5))
print(myRect.collidepoint(6,6))
print(myRect.collidepoint(7,7))
print(myRect.collidepoint(9,9))

"""
Web:
Requests: https://pypi.org/project/requests/
Django: https://pypi.org/project/Django/
Flask: https://pypi.org/project/Flask/
Twisted: https://twistedmatrix.com/trac/                    game backgroud comunication
BeautifulSoup: https://pypi.org/project/beautifulsoup4/
Selenium: https://selenium-python.readthedocs.io/

Data science:
Numpy: https://numpy.org/
Pandas: https://pandas.pydata.org/
Matplotlib: https://matplotlib.org/
Nltk: https://www.nltk.org/
Opencv: https://opencv-python-tutroals.readth...

Machine Learning:
Tensorflow: https://www.tensorflow.org/
Keras: https://keras.io/
PyTorch: https://pytorch.org/
Sci-kit Learn: https://scikit-learn.org/stable/

GUI:
Kivy: https://kivy.org/#home
PyQt5: https://pypi.org/project/PyQt5/
Tkinter: https://wiki.python.org/moin/TkInter

Bonus:
Pygame: https://www.pygame.org/docs/
"""
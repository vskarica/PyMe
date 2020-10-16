def f():
    return 555
a=type("a",(),{
    "a":1,
    "b":2,
    "c":f})

#print(a.c())
class b:
    a=[]
    def __init__(self):
        self.aa=len(b.a)+10
        b.a.append(self)
    def b():
        return a

c=b()
cc=b()
ccc=b()
cccc=b()
print(b.a[0].aa)



g="f()"
try:
    print(2*eval(g))
except(NameError):
    pass
#getattr(main, g)()
c=6
def fun(a=0,b=0,c=0):
    print(a,b,c)
#x=[4,5,6]
x={"a":4,"b":5,"c":6}
fun(c=3,b=2)
fun(**x)
print(c)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#deklaracije i izvršavanje funkcije iz stringa
import inspect
lines = inspect.getsource(f)
#print(lines)
lines=lines[:4]+"h"+lines[5:]
print(lines)
exec(lines)
print(h())

lines = inspect.getsource(b)
lines=lines[:6]+"b2"+lines[7:]
exec(lines)
print(b.a)

#DEKORACIJE
import functools    # za @functools.wraps(func)

def uokviri(func):
    @functools.wraps(func)  #dekoracija koja pomaže sačuvati metapodatke originalne funkcije
    def wrapper(*args, **kwargs):
        print("*************************")
        func(*args, **kwargs)
        print("*************************")
    return wrapper

@uokviri
def pprint(nešto):
    print(f"Evo {nešto} za isprintati")

#pprint()
pprint("kuća")


def putax(x=2):
    def w1(f):
        def w2(*args, **kwargs):
            for i in range(x):
                f(*args, **kwargs)
        return w2
    return w1
class PutaX(object):
    """def __init__(self,f,x=2):
        self.f=f
        self.x=x
    def __call__(self,*args, **kwargs):
        for i in range(self.x):
            self.f(*args, **kwargs)"""
    def __init__(self,x=2):
        self.x=x
    def __call__(self,f):
        def wrapper(*args, **kwargs):
            for i in range(self.x):
                f(*args, **kwargs)
        return wrapper

@putax
def ppprint(nešto):
    print(f"Evo {nešto} za isprintati")

ppprint("žaba")


# PythonDecorators/decorator_with_arguments.py
"""class decorator_with_arguments(object):

    def __init__(self, arg1, arg2, arg3):

        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):

        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decorator_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")"""
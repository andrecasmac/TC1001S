from turtle import *
from freegames import floor, vector

comparador = True
llave = False
path = Turtle(visible=False)

mapa = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
]


def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(24)
        path.left(90)

    path.end_fill()

def world():
    "Draw world using path."
    bgcolor('green')

    for index in range(len(mapa)):
        tile = mapa[index]

        if tile == 1:
            path.color('grey')
            x = (index % 25) * 25 - 310
            y = 290 - (index // 25) * 25
            square(x, y)
        elif tile == 2:
            path.color('red')
            x = (index % 25) * 25 - 310
            y = 290 - (index // 25) * 25
            square(x, y)
        elif tile == 3:
            path.color('brown')
            x = (index % 25) * 25 - 310
            y = 290 - (index // 25) * 25
            square(x, y)
        elif tile == 4:
            path.color('yellow')
            x = (index % 25) * 25 - 310
            y = 290 - (index // 25) * 25
            square(x, y)


def encontrar(lista):
    for v in range(625):
        if lista[v] == 2:
            return v
        else: 
            continue
        

def arriba():
    posicion = encontrar(mapa)
    global llave
    if (mapa[posicion-25] == 1):
        mapa[posicion-25] = 2
        mapa[posicion] = 1
    elif (mapa[posicion-25] == 4):
        mapa[posicion-25] = 2
        mapa[posicion] = 1
        llave = True
    elif (mapa[posicion-25] == 3 and llave == True):
        mapa[posicion-25] = 2
        mapa[posicion] = 1
        tracer(False)
        world() 
        done()
 

def izquierda():
    posicion = encontrar(mapa)
    global llave
    if (mapa[posicion-1] == 1):
        mapa[posicion-1] = 2
        mapa[posicion] = 1
    elif (mapa[posicion-1] == 4):
        mapa[posicion-1] = 2
        mapa[posicion] = 1
        llave = True
    elif (mapa[posicion-1] == 3 and llave == True):
        mapa[posicion-1] = 2
        mapa[posicion] = 1
        tracer(False)
        world() 
        done()
  


def abajo():
    posicion = encontrar(mapa)
    global llave
    if (mapa[posicion+25] == 1):
        mapa[posicion+25] = 2
        mapa[posicion] = 1
    elif (mapa[posicion+25] == 4):
        mapa[posicion+25] = 2
        mapa[posicion] = 1
        llave = True
    elif (mapa[posicion+25] == 3 and llave == True):
        mapa[posicion+25] = 2
        mapa[posicion] = 1
        tracer(False)
        world() 
        done()


def derecha():
    posicion = encontrar(mapa)
    global llave
    if (mapa[posicion+1] == 1):
        mapa[posicion+1] = 2
        mapa[posicion] = 1
    elif (mapa[posicion-1] == 4):
        mapa[posicion-1] = 2
        mapa[posicion] = 1
        llave = True
    elif (mapa[posicion+1] == 3 and llave == True):
        mapa[posicion+1] = 2
        mapa[posicion] = 1
        tracer(False)
        world() 
        done()


setup(700, 700)
hideturtle()
while comparador == True:
    tracer(False)
    world()  
    listen() 
    onkeypress(arriba, 'w')
    onkeypress(abajo, 's')
    onkeypress(derecha, 'd')
    onkeypress(izquierda, 'a')
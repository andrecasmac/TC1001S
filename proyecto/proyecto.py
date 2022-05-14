# Equipo 4
# Integrantes:
# A01254180 - André Castillo Machado
# A01254155 - Marco Tulio Montoya Angulo
# A00835132 - Ángel de Fidel Marín González
# A01254831 - Luis Carlos Rico Almada

# Proyecto TC1001S - Laberinto

from turtle import *
from freegames import floor, vector
import random

# Se definen variables
comparador = True
llave = False
path = Turtle(visible=False)

# Creación de mapas
# Hecho por: Marco Montoya
mapa = []

mapa1 = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 4, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
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

mapa2 = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 4, 0, 1, 0, 1, 0, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,
]


# Se selecciona de manera aleatoria el mapa
# Hecho por: Luis Rico
n_random = random.randint(0,1)
if n_random == 0:
    mapa = mapa1
elif n_random == 1:
    mapa = mapa2

# Funcion para dibujar un cuadrado en el mundo
# Hecho por: Marco Montoya
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):  # Se dibuja el cuadro por partes
        path.forward(24)
        path.left(90)

    path.end_fill()


# Se crea el "mundo" usando las funciones de turtle
# Hecho por: Ángel Marín
def world():
    "Draw world using path."
    bgcolor('chartreuse3')

    for index in range(len(mapa)):
        tile = mapa[index]

        if tile == 1:
            path.color('bisque')    # Se define el color del cuadro
            x = (index % 25) * 25 - 310     # Coordenadas del cuadro
            y = 290 - (index // 25) * 25
            square(x, y)
        elif tile == 2:
            path.color('red')
            x = (index % 25) * 25 - 310
            y = 290 - (index // 25) * 25
            square(x, y)
        elif tile == 3:
            path.color('saddlebrown')
            x = (index % 25) * 25 - 310
            y = 290 - (index // 25) * 25
            square(x, y)
        elif tile == 4:
            path.color('gold')
            x = (index % 25) * 25 - 310
            y = 290 - (index // 25) * 25
            square(x, y)

# Se busca la posicion actual del personaje
# Hecho por: Marco Montoya
def encontrar(lista):
    for v in range(625):
        if lista[v] == 2:
            return v
        else: 
            continue
        
# Funciones para mover al personaje dentro del laberinto
# Hecho por: André Castilo

# Ejemplo base:
def arriba():
    posicion = encontrar(mapa)  # Se obtiene la posicion del personaje
    global llave
    if (mapa[posicion-25] == 1):
        mapa[posicion-25] = 2   
        mapa[posicion] = 1      # Se modifica la matriz
    elif (mapa[posicion-25] == 4):
        mapa[posicion-25] = 2
        mapa[posicion] = 1
        llave = True
    elif (mapa[posicion-25] == 3 and llave == True):
        mapa[posicion-25] = 2
        mapa[posicion] = 1
        tracer(False)
        world()         
        done()  # Se acaba el juego

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
    elif (mapa[posicion+1] == 4):
        mapa[posicion+1] = 2
        mapa[posicion] = 1
        llave = True
    elif (mapa[posicion+1] == 3 and llave == True):
        mapa[posicion+1] = 2
        mapa[posicion] = 1
        tracer(False)
        world() 
        done()



# Se genera la ventana del turtle
# Hecho por: Ángel Marín
setup(700, 700)
hideturtle()

# Ciclo while que repite el ciclo cada que se presiona una tecla
# Hecho por: André Castillo
while comparador == True:
    tracer(False)
    world()     # Se dibuja el mundo
    listen() 
    onkeypress(arriba, 'w')     # Detección de teclas oprimidas
    onkeypress(abajo, 's')
    onkeypress(derecha, 'd')
    onkeypress(izquierda, 'a')
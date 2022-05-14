# Equipo 4
# Integrantes:
# A01254180 - André Castillo Machado
# A01254155 - Marco Tulio Montoya Angulo
# A00835132 - Ángel de Fidel Marín González
# A01254831 - Luis Carlos Rico Almada

# Proyecto TC1001S - Laberinto
#Se importan librerias
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
mapa3 = [
    3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,
    0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,
    0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,
    0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,
    0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,
    0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,
    0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,
    0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,
    0,1,1,1,1,1,1,1,1,1,0,4,0,1,1,1,1,1,1,1,0,1,0,1,0,
    0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,
    0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,
    0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,
    0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,
    0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,
    0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,
    0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,
    0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,
    0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,
    0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,
    0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,
    0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,
    0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,
    0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,
]

# Se selecciona de manera aleatoria el mapa
# Hecho por: Luis Rico
n_random = random.randint(0,2)
if n_random == 0:
    mapa = mapa1
elif n_random == 1:
    mapa = mapa2
elif n_random == 2:
    mapa = mapa3

def Pantalla_win(): #Pantalla final, cuando llegas al cuadro amarrillo aparece esta pantalla
    setup(700, 700) #Hecho por: Luis Rico
    bgcolor("black")
    write("GANASTE, FEELICIDADES, COMPLETASTE EL MAPA", color("white"), font=("Arial",20,"normal"),align="center")

# Funcion para dibujar un cuadrado en el mundo
# Hecho por: Angel Marin
def square(x, y):

    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):  # Se dibuja el cuadro por partes
        path.forward(24) #dimension del cuadrado
        path.left(90) #angulo del cuadrado

    path.end_fill()


# Se crea el "mundo" usando las funciones de turtle
# Hecho por: Ángel Marín
def world():

    bgcolor('chartreuse3') #color del fondo

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
    elif (mapa[posicion-25] == 3 and llave == True): #Cuando el personaje llega a la puerta
        mapa[posicion-25] = 2
        mapa[posicion] = 1
        tracer(False)
        Pantalla_win() #Se inicia la pantalla de finalizar
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
        Pantalla_win() 
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
        Pantalla_win()
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
        Pantalla_win() 
        done()



# Se genera la ventana del turtle
# Hecho por: Marco Montoya
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
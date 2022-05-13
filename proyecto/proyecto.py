from turtle import *

comparador = True

mapa = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]



while comparador == True:
    comparador2 = True
    print(mapa)
    for x in range(20):
        for y in range(20):
            if mapa[x][y] == 0:
                print("#", end="")
            elif mapa[x][y] == 1:
                print("X", end="")
            elif mapa[x][y] == 2:
                print("v", end="")
        print("")

    tecla = input()

    break_out_flag = False
    for i in range(20):
        for j in range(20):
            if mapa[i][j] == 2:
                if tecla == "w":
                        if (mapa[i-1][j] == 1):
                            mapa[i-1][j] = 2
                            mapa[i][j] = 1
                        elif (mapa[i-1][j] == 3):
                            mapa[i-1][j] = 2
                            mapa[i][j] = 1
                            comparador = False
                        else:
                            continue
                elif tecla == "a":
                        if (mapa[i][j-1] == 1):
                            mapa[i][j-1] = 2
                            mapa[i][j] = 1
                        elif (mapa[i][j-1] == 3):
                            mapa[i][j-1] = 2
                            mapa[i][j] = 1
                            comparador = False
                        else:
                            continue
                elif tecla == "s":
                    if (mapa[i+1][j] == 1):
                        mapa[i+1][j] = 2
                        mapa[i][j] = 1
                        print("bajé")
                        break_out_flag = True
                        break
                    elif (mapa[i][j-1] == 3):
                        mapa[i+1][j-1] = 2
                        mapa[i+1][j] = 1
                        comparador = False
                    else:
                        continue
                elif tecla == "d":
                    if (mapa[i][j+1] == 1):
                        mapa[i][j+1] = 2
                        mapa[i][j] = 1
                        break
                    elif (mapa[i][j+1] == 3):
                        mapa[i][j+1] = 2
                        mapa[i][j] = 1
                        comparador = False
                    else:
                        continue
                else:
                    print("Tecla inválida")
            else:
                continue
        if break_out_flag:
            break
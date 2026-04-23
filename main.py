from Hundir_La_Flota_Ander.utils import (crear_tablero, mostrar_tablero, colocar_barcos, crear_lista_barcos, disparar, agua, barco, tocado, fallo)

import numpy as np
import time

#TABLEROS VACIOS DE LOS 2 JUGADORES
tablero_jugador = crear_tablero()
tablero_oponente = crear_tablero()

#TABLEROS DISPAROS DE LOS 2 JUGADORES
tablero_jugador_disparos = crear_tablero()
tablero_oponente_disparos = crear_tablero()

print("\nWELCOME TO HUNDIR EL BARCO 🚢 :)\n")

print("COLOCA TUS BARCOS!!")
tablero_jugador=colocar_barcos(tablero_jugador, lista_barcos_jugador)
tablero_oponente=colocar_barcos(tablero_oponente,lista_barcos_oponente)    


#OPONENTE PONE COLOCA SUS BARCOS
lista_barcos_jugador=crear_lista_barcos()
lista_barcos_oponente=crear_lista_barcos()


turno = 1

#DINAMICA DEL JUEGO
while True: 
    
    print("\nTABLERO DE TUS BARCOS")
    mostrar_tablero(tablero_jugador)

    print("TABLERO DE TUS DISPAROS")
    mostrar_tablero(tablero_jugador_disparos)

    #TURNO DEL JUGADOR
    print("TU TURNO!! TURNO Nª:",turno)
    print("A DISPARAR!!!\n")
    tablero_oponente,tablero_jugador_disparos,resultado=disparar(tablero_oponente,tablero_jugador_disparos,lista_barcos_oponente)

    #BUCLE POR SI DISPARA EN LA MISMA CELDA
    while resultado=="repetido":
        tablero_oponente, tablero_jugador_disparos,resultado=disparar(tablero_oponente,tablero_jugador_disparos,lista_barcos_oponente)

    time.sleep(2)

    #COMPROBACION TU VICTORIA
    if not np.any(tablero_oponente==barco):
        print("VICTORIAA!!!\n")
        print("TABLERO FINAL DEL OPONENTE")
        mostrar_tablero(tablero_oponente)
        break

    # -----------------------------------------
    #TURNO DEL OPONENTE
    print("\nTURNO DEL OPONENTE")

    disparo_valido= False

    while not disparo_valido:
        fila=np.random.randint(0,10)
        columna=np.random.randint(0,10)

        if tablero_oponente_disparos[fila][columna]==agua:
            disparo_valido=True
    
    if tablero_jugador[fila][columna]==barco:
        tablero_jugador[fila][columna]=tocado
        tablero_oponente_disparos[fila][columna]=tocado
        print("EL OPONENTE HA TOCADO ;(")
    else:
        tablero_jugador[fila][columna]=fallo
        tablero_oponente_disparos[fila][columna]=fallo
        print("EL OPONENTE HA FALLADO!! :)\n")

    time.sleep(2)

    # -----------------------------------------
    #COMPROBACION VICTORIA OPONENTE
    if not np.any(tablero_jugador==barco):
        print("EL OPONENTE HA GANADO")
        print("\n TABLERO FINAL DEL JUGADOR")
        mostrar_tablero(tablero_jugador)
        break
    
    turno+=1

print("FIN DEL JUEGO")
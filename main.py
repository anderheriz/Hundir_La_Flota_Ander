from utils_tableros import (crear_tablero, mostrar_tablero, colocar_barcos, crear_lista_barcos, colocar_barcos_jugador, barco)
from utils_juego import (turno_jugador, turno_oponente)

import numpy as np
import time

#TABLEROS VACIOS DE LOS 2 JUGADORES
tablero_jugador = crear_tablero()
tablero_oponente = crear_tablero()

#TABLEROS DISPAROS DE LOS 2 JUGADORES
tablero_jugador_disparos = crear_tablero()
tablero_oponente_disparos = crear_tablero()

print("\nWELCOME TO HUNDIR LA FLOTA 🚢 :)\n")

#LLAMADA A LA FUNCION PARA COLOCAR BARCOS MANUALMENTE
tablero_jugador, lista_barcos_jugador = colocar_barcos_jugador(tablero_jugador) 

#OPONENTE COLOCA SUS BARCOS AUTOMATICAMENTE
lista_barcos_oponente=crear_lista_barcos()
tablero_oponente=colocar_barcos(tablero_oponente, lista_barcos_oponente)

turno = 1

#DINAMICA DEL JUEGO - BUCLE PRINCIPAL   
while True: 
    
    print("\n" + "TABLERO DE MIS BARCOS\n")
    mostrar_tablero(tablero_jugador, separador = False)

    print("\n" + "TABLERO DE MIS DISPAROS\n")
    mostrar_tablero(tablero_jugador_disparos, separador = False)
    print("\n"+ "-"*25)

    #TURNO DEL JUGADOR
    print("\n" + f"TU TURNO - Nª:{turno}".center(26,"="))
    print("A DISPARAR!!!\n")
    tablero_oponente,tablero_jugador_disparos,resultado= turno_jugador(tablero_oponente,tablero_jugador_disparos,lista_barcos_oponente)

    time.sleep(2)

    #COMPROBACION TU VICTORIA 
    if not np.any(tablero_oponente == barco):
        print("VICTORIAA!!!  ✅ ✅ ✅\n")
        print("TABLERO FINAL DEL OPONENTE")
        mostrar_tablero(tablero_oponente)
        break

    # -----------------------------------------
    #TURNO DEL OPONENTE
    print("\n"+"TURNO DEL OPONENTE:".center(26,"="))
    tablero_jugador, tablero_oponente_disparos = turno_oponente(tablero_jugador, tablero_oponente_disparos)

    time.sleep(2)

    # -----------------------------------------
    #COMPROBACION VICTORIA OPONENTE
    if not np.any(tablero_jugador == barco):
        print("EL OPONENTE HA GANADO")
        print("\nTABLERO FINAL DEL JUGADOR")
        mostrar_tablero(tablero_jugador)
        break
    
    turno+=1

print("FIN DEL JUEGO")
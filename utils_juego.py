import numpy as np
from utils_tableros import agua, barco, tocado, fallo

#FUNCION AUXILIAR PARA DISPARAR -> COMPROBACION BARCO HUNDIDO
def barco_hundido(celda, lista_barcos, tablero): 
    """ Mira la celda impactada y busca a qué barco pertenece. Una vez lo encuentra, recorre todas sus posiciones y comprueba 
    si todas están marcadas como tocadas en el tablero. Si alguna no lo está, devuelve False, pero si todas lo están, 
    devuelve True, indicando que el barco está hundido.”"""
    for un_barco in lista_barcos:
        if celda in un_barco:
            for posicion in un_barco:
                if tablero[posicion] != tocado:
                    return False
            return True #si todas las posiciones del barco estan tocadas, i.e. hundido.    

def disparar(tablero_objetivo, tablero_disparos, lista_barcos):   
    '''pedir coordenadas, validar el input y marcar si es agua, tocado, hundido o repetido.'''
    valido= False

    while not valido:
        try:
            fila=int(input("Fila: "))
            columna= int(input("Columna: "))

            if 0 <= fila <10 and 0 <= columna <10:
                valido = True
            else:
                print("Coordenadas fuera de rango")
        except ValueError:
            print("Debes introducir numeros")


    if tablero_disparos[fila][columna] in [tocado, fallo]:
        print("YA HABIAS DISPARADO AHI!!")
        return tablero_objetivo, tablero_disparos, "repetido"

    elif tablero_objetivo[fila][columna]==barco:
        tablero_objetivo[fila][columna]= tocado
        tablero_disparos[fila][columna]= tocado

        if barco_hundido((fila,columna),lista_barcos,tablero_objetivo):
            print("TOCADO y HUNDIDO :)  ✅ ✅ ")
            return tablero_objetivo, tablero_disparos, "hundido"
        else:
            print("TOCADO :)  ✅")  
            return tablero_objetivo, tablero_disparos, "tocado"

    elif tablero_objetivo[fila][columna]==agua:
        tablero_objetivo[fila][columna]= fallo
        tablero_disparos[fila][columna]= fallo
        print("AGUA 🌊")
        return tablero_objetivo, tablero_disparos, "agua"

    
def turno_jugador(tablero_oponente, tablero_jugador_disparos, lista_barcos_oponente):
    '''Gestiona el turno del jugador y si dispara a una celda repetida, le obliga a volver a disparar.'''
    tablero_oponente, tablero_jugador_disparos, resultado = disparar(   #ejecuta el disparo
        tablero_oponente, tablero_jugador_disparos, lista_barcos_oponente) 
    
    while resultado == "repetido": #verificar que no disparar 2 veces en la misma celda 
        tablero_oponente, tablero_jugador_disparos, resultado = disparar(
            tablero_oponente, tablero_jugador_disparos, lista_barcos_oponente)
    
    return tablero_oponente, tablero_jugador_disparos, resultado


def turno_oponente(tablero_jugador, tablero_oponente_disparos): 
    '''Hace que el oponente dispare automáticamente a una celda aleatoria no usada y actualiza el resultado del disparo.'''
    disparo_valido = False
    
    while not disparo_valido:
        fila = np.random.randint(0,10)
        columna = np.random.randint(0,10)

        if tablero_oponente_disparos[fila][columna] == agua:
            disparo_valido = True
    
    if tablero_jugador[fila][columna] == barco:
        tablero_jugador[fila][columna] = tocado
        tablero_oponente_disparos[fila][columna] = tocado
        print("EL OPONENTE HA TOCADO ;(")
    
    else:
        tablero_jugador[fila][columna] = fallo
        tablero_oponente_disparos[fila][columna] = fallo
        print("EL OPONENTE HA FALLADO :) ")
    
    return tablero_jugador, tablero_oponente_disparos
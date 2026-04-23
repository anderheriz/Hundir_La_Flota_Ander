import numpy as np

#SIMBOLOS DENTRO DEL TABLERO
agua="_"
barco="O"
tocado="X"
fallo="#"

#TAMAÑO ESLORAS
esloras=[2,2,2,3,3,4]

def crear_tablero(tamaño=10):
    '''Crea un tablero donde cada posicion esta vacia al inicio, que significa agua. Esto sirve para empezar con el tablero del jugador, 
    tablero del oponente y el tablero de los disparos.
    '''
    return np.full((tamaño,tamaño),agua)   

def mostrar_tablero(tablero,ocultar_barcos=False, separador=True):  
    """ La función hace esto:
            1. imprime los indices de las columnas
            2. recorre cada fila del tablero
            3. recorre cada celda de esa fila
            4. si hay que ocultar barcos, cambia el "O"(barco) por " " (agua).
            5. guarda la fila en una lista
            6. imprime esa fila con su indice
    """
    print("  ",end="") 
    for i in range (len(tablero[0])):
        print(i,end=" ")
    print()

    for i, fila in enumerate(tablero):
        fila_mostrar=[]
        for celda in fila:
            if ocultar_barcos and celda==barco:  #Si ocultar_barcos vale True, sustituye visualmente los barcos por agua.
                fila_mostrar.append(agua) 
            else:
                fila_mostrar.append(celda)
        print (str(i)+" "+ " ".join(fila_mostrar))  #Convierte el índice de fila a texto con str(i).
    if separador:
        print("-"*25)
    
#CREACION DE BARCOS EN EL TABLERO
def crear_barcos(eslora,tamaño=10):  
    """Esta función genera un barco aleatorio. Primero decide su orientación, luego elige una posición inicial 
    que no se salga del tablero y finalmente construye el barco añadiendo posiciones consecutivas según su tamaño."""
    lista_barco=[]

    orientacion=np.random.choice(["H","V"])

    if orientacion== "H":
        fila= np.random.randint(0,tamaño)
        columna= np.random.randint(0,tamaño - eslora + 1)
        for i in range(eslora):
            lista_barco.append((fila, columna + i)) 
    
    else:
        fila= np.random.randint(0,tamaño - eslora + 1)
        columna= np.random.randint(0,tamaño)
        for i in range(eslora):
            lista_barco.append((fila + i, columna))
 
    return lista_barco #devulves la lista con las coordenadas de los barcos  

#COMPROBACION QUE LOS BARCOS NO SALGAN DEL TABLERO Y QUE NO SE SOLAPEN
def barco_valido(lista_barco, tablero, tamaño=10):  
    for fila, columna in lista_barco:  
        if fila <0 or fila>=tamaño or columna < 0 or columna >=tamaño:
            return False
        if tablero[fila][columna]==barco:
            return False
    return True


# COLOCA EN EL TABLERO LA LISTA DE BARCOS 
def colocar_barcos(tablero, lista_barcos): 
    '''Recorre cada barco y cada celda de ese barco para dibujarlo en el tablero.'''
    for un_barco in lista_barcos:
        for celda in un_barco:
            tablero[celda]= barco
    return tablero


#CREA LOS BARCOS AUTOMATICOS DEL OPONENTE Y DEMO-> Es dependiente de crear_tablero(), crear_barcos(), barco_valido(), colocar_barcos()
def crear_lista_barcos(eslora=None, tamaño=10): 
    """ Genera una lista de barcos válidos usando posiciones aleatorias hasta completar todas las esloras, cumpliendo que los barcos
    no se salgan del tablero, ni se pisen entre ellos."""
    if eslora is None:
        eslora=esloras
    
    tablero_ayuda=crear_tablero(tamaño)  #solo sirve para validar que los barcos no se pisan
    lista_barcos=[]  #aqui se guardan los barcos validos

    for eslora_barco in eslora:
        valido = False #antes de intentar colocar cada barco, asumes que todavía no has conseguido uno válido.

        while not valido:  #este while genera barcos hasta que busque los validos
            nuevo_barco=crear_barcos(eslora_barco,tamaño)   

            if barco_valido(nuevo_barco,tablero_ayuda,tamaño):
                '''Aqui se validan los barcos y guardarlos en la lista fiinal'''
                lista_barcos.append(nuevo_barco)
                colocar_barcos(tablero_ayuda,[nuevo_barco]) #mete barcos 
                valido=True #
    
    return lista_barcos

#COLOCACION BARCOS DEL JUGADOR AL INICIO DE LA PARTIDA
def colocar_barcos_jugador(tablero):
    ''' Se pide al usuaruio la posicion de los barcos y se valida que se hayan colocado correctamente.'''
    lista_barcos=[]

    for eslora_barco in esloras:
        valido = False #antes de intentar colocar cada barco, asumes que todavía no has conseguido uno válido.

        while not valido: #este while genera barcos hasta que los barcos esten bien colocados
            print("\n"+ "MI TABLERO".center(23,"="))
            mostrar_tablero(tablero,separador=False) #sirve para que el jugador sepa donde ya ha puesto los barcos antes de poner el siguiente.

            print()
            print(f"Coloca un barco de eslora: {eslora_barco}")

            coordenadas_validas = False #controla si la fila y la columna que escribes son correctas o no

            while not coordenadas_validas:
                try:
                    fila = int(input("Fila inicial (0-9): "))
                    columna = int(input("Columna inicial (0-9): "))

                    if 0 <= fila < 10 and 0 <= columna <10:
                        coordenadas_validas = True
                    else:
                        print("Fuera de rango (0-9) Repite!!")

                except ValueError:
                    print("INVALIDO!. Debes introducir numeros.")

            orientacion_valida = False

            while not orientacion_valida:
                orientacion = input("Orientacion (H/V): ").upper()

                if orientacion in ["H", "V"]:
                    orientacion_valida = True
                else:
                    print("Orientacion invalida. Escribe H o V\n")

            nuevo_barco = []

            if orientacion == "H":
                for i in range(eslora_barco):
                    nuevo_barco.append((fila, columna + i))
            
            else:
                for i in range(eslora_barco):
                    nuevo_barco.append((fila + i, columna))
            
            if barco_valido(nuevo_barco,tablero):
                lista_barcos.append(nuevo_barco)
                colocar_barcos(tablero, [nuevo_barco])
                valido = True
            else:
                print("\nPosicion invalida. REPITE!")
    
    return tablero, lista_barcos

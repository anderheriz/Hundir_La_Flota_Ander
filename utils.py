import numpy as np

agua="_"
barco="O"
tocado="X"
fallo="#"

esloras=[2,2,2,3,3,4]

def crear_tablero():
    '''Crea un tablero donde cada posicion esta vacia al inicio, que significa agua. Esto sirve para empezar con el tablero del jugador, 
    tablero del oponente y el tablero de los disparos.
    '''
    return np.full((10,10),agua)   

def mostrar_tablero(tablero,ocultar_barcos=False):  
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
            if ocultar_barcos and celda==barco:
                fila_mostrar.append(agua)
            else:
                fila_mostrar.append(celda)
        print (str(i)+" "+ " ".join(fila_mostrar))
    
    print("-"*40)

def crear_barcos(eslora):  
    """Esta función genera un barco aleatorio. Primero decide su orientación, luego elige una posición inicial 
    que no se salga del tablero y finalmente construye el barco añadiendo posiciones consecutivas según su tamaño."""
    lista_barco=[]

    orientacion=np.random.choice(["H","V"])

    if orientacion== "H":
        fila= np.random.randint(0,10)
        columna= np.random.randint(0,10-eslora+1)
        for i in range(eslora):
            lista_barco.append((fila, columna + i)) 
    
    else:
        fila= np.random.randint(0,10-eslora)
        columna= np.random.randint(0,10)
        for i in range(eslora):
            lista_barco.append((fila + i, columna))
 
    return lista_barco #devuelve la lista con las coordenadas

def barco_valido(lista_barco, tablero):  #comprobacion si barcos se solapan
    for fila, columna in lista_barco:    #barco es una lista de coordenadas
        if fila <0 or fila>=10 or columna < 0 or columna >=10:
            return False
        if tablero[fila][columna]==barco:
            return False
    return True


def colocar_barcos(tablero, lista_barcos): #coloca en el tablero una lista de barcos
    for un_barco in lista_barcos:
        for celda in un_barco:
            tablero[celda]= barco
    return tablero

def crear_lista_barcos(): #devuelve todos los barcos del juego en una lista (que tiene sublistas, que representa cada barco)
    tablero_ayuda=crear_tablero()  #solo sirve para validar barcos
    lista_barcos=[]  #aqui se guardan los barcos validos

    for eslora_barco in esloras:
        valido = False

        while not valido:  #este while genera barcos hasta que uno sea valido
            nuevo_barco=crear_barcos(eslora_barco)   

            if barco_valido(nuevo_barco,tablero_ayuda):
                lista_barcos.append(nuevo_barco)
                colocar_barcos(tablero_ayuda,[nuevo_barco])
                valido=True #salir del while
    
    return lista_barcos

def colocar_barcos_jugador(tablero):
    lista_barcos=[]

    for eslora_barco in esloras:
        valido = False

        while not valido:
            mostrar_tablero(tablero)
            print(f"\n Coloca un barco de eslora: {eslora_barco}")

            fila = int(input("Fila inicial: "))
            columna = int(input("Columna inicial: "))
            orientacion = input("orientacion (H/V): ").upper()

            nuevo_barco = []

            if orientacion == "H":
                for i in range(eslora_barco):
                    nuevo_barco.append((fila, columna + i))

            else:
                for i in range(eslora,barco):
                    nuevo_barco.append((fila+i, columna))
            
            if barco_valido(nuevo_barco,tablero):
                lista_barcos.append(nuevo_barco)
                colocar_barcos(tablero, [nuevo_barco])
                valido = True
            else:
                pritn("Barco invalido X ")
    
    return tablero, lista_barcos

def barco_hundido(celda, lista_barcos, tablero):
    for un_barco in lista_barcos:
        if celda in un_barco:
            for posicion in un_barco:
                if tablero[posicion] != tocado:
                    return False
            return True


def disparar(tablero_objetivo, tablero_disparos,lista_barcos):   #pedir coordenadas y marcar si es tocado, agua o repetido.
    fila=int(input("fila: "))
    columna= int(input("columna: "))
    
    if tablero_disparos[fila][columna]!=agua:
        print("YA HABIAS DISPARADO AHI!!")
        return tablero_objetivo, tablero_disparos, "repetido"

    elif tablero_objetivo[fila][columna]==barco:
        tablero_objetivo[fila][columna]= tocado
        tablero_disparos[fila][columna]= tocado

        if barco_hundido((fila,columna),lista_barcos,tablero_objetivo):
            print("TOCADO y HUNDIDO :))")
            return tablero_objetivo, tablero_disparos, "hundido"
        else:
            print("TOCADO :)")
            return tablero_objetivo, tablero_disparos, "tocado"

    elif tablero_objetivo[fila][columna]==agua:
        tablero_objetivo[fila][columna]= fallo
        tablero_disparos[fila][columna]= fallo
        print("AGUA")
        return tablero_objetivo, tablero_disparos, "agua"

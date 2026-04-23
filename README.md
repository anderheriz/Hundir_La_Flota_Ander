# Hundir La Flota

Implementación en Python del juego Hundir la Flota para ejecución en terminal. El jugador se enfrenta a un oponente automático, colocando sus barcos y realizando disparos por turnos hasta hundir toda la flota rival.

## Descripción

El juego se desarrolla en un tablero de 10x10.
El jugador coloca sus barcos manualmente indicando fila, columna y orientación, mientras que el oponente los genera de forma aleatoria. Durante la partida, ambos realizan disparos alternos y el sistema informa del resultado de cada uno (agua, tocado o hundido).

La partida finaliza cuando uno de los dos jugadores pierde todos sus barcos.

## Estructura del proyecto

* `main.py`
  Gestiona el flujo principal del juego: inicialización de tableros, colocación de barcos, turnos y comprobación de victoria.

* `utils_tableros.py`
  Contiene funciones para la creación y representación del tablero, generación de barcos, validación de posiciones y colocación en el tablero.

* `utils_juego.py`
  Incluye la lógica de la partida: gestión de disparos, detección de impactos y control de los turnos del jugador y del oponente.

## Uso

Ejecutar el archivo principal:

```bash id="7e7n02"
python main.py
```

Seguir las instrucciones en terminal para colocar los barcos y realizar los disparos.

## Requisitos

* Python 3.10 o superior
* numpy


# Juego de Tic Tac Toe en la Terminal - V2 (Imbatible, usando Minimax)

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

Este proyecto es una versión avanzada del juego de **[Tic Tac Toe](https://github.com/VintaBytes/tic-tac-toe-V1/blob/main/README.md)** en Python. A diferencia de la primera versión, donde la computadora elegía movimientos de manera aleatoria, aquí se implementa el algoritmo **Minimax**, que le permite a la computadora tomar decisiones óptimas en cada turno, haciéndola prácticamente imbatible.


<span><img src="https://github.com/VintaBytes/tic-tac-toe-V2/blob/main/tictactoe2.png?raw=true"/></span>

## Descripción del Código

El código sigue una estructura modular, con varias funciones que permiten gestionar el flujo del juego, verificar las condiciones de victoria o empate, y tomar decisiones estratégicas utilizando el algoritmo **Minimax**.

### Función: `mostrar_tablero(tablero)`

Esta función imprime el tablero actual del juego en la terminal, utilizando la biblioteca **Colorama** para colorear las celdas. Las **X** se muestran en rojo, las **O** en verde, y las líneas divisorias del tablero se muestran en ámbar (color amarillo). Esto facilita que el usuario vea de manera clara y visualmente atractiva el estado del juego.

### Función: `mostrar_celda(celda)`

Esta función devuelve la representación de cada celda con su respectivo color. Si la celda contiene una **X**, la devuelve en rojo; si contiene una **O**, la devuelve en verde. Las celdas vacías se representan con `"-"` sin ningún color.

### Función: `verificar_ganador(tablero, jugador)`

Esta función verifica si hay un ganador. Utiliza las combinaciones ganadoras clásicas de Tic Tac Toe (filas, columnas y diagonales) y compara las posiciones del tablero. Si encuentra una combinación en la que las tres celdas contienen el símbolo del jugador actual, devuelve `True`, indicando que ese jugador ha ganado. De lo contrario, devuelve `False`.

### Función: `tablero_lleno(tablero)`

Esta función revisa si el tablero está completamente lleno. Si todas las celdas están ocupadas y no queda ninguna libre, devuelve `True`, lo que indica que el juego ha terminado en empate. Si aún hay celdas vacías, devuelve `False`.

### Algoritmo Minimax

El **algoritmo Minimax** es el núcleo de esta versión del juego, y es el responsable de hacer que la computadora sea casi imbatible. El propósito de este algoritmo es evaluar todas las posibles jugadas futuras y escoger la que maximiza las probabilidades de ganar para la computadora (jugando con "O") y minimiza las probabilidades de perder frente al jugador humano (jugando con "X").

#### Funcionamiento del Minimax

El Minimax funciona utilizando un enfoque recursivo. En cada turno, se simulan todas las jugadas posibles para evaluar cuál es la mejor. La computadora maximiza su ganancia (es decir, busca ganar) y el jugador humano minimiza la ganancia de la computadora (intenta evitar perder).

- **Estado terminal**: Si en un estado del tablero, la computadora ha ganado, el valor de ese estado es **1**. Si el jugador humano ha ganado, el valor del estado es **-1**. Si el juego termina en empate, el valor es **0**.
  
- **Recursividad**: En cada estado del tablero, el algoritmo explora todas las posibles jugadas restantes. Si es el turno de la computadora, selecciona el valor máximo de los posibles resultados futuros. Si es el turno del jugador humano, selecciona el valor mínimo.
  
El siguiente bloque de código implementa el algoritmo Minimax:

```python
def minimax(tablero, es_maximizar):
    if verificar_ganador(tablero, 'O'):
        return 1  # Gana la computadora
    if verificar_ganador(tablero, 'X'):
        return -1  # Gana el jugador humano
    if tablero_lleno(tablero):
        return 0  # Empate

    if es_maximizar:
        mejor_puntaje = -float('inf')
        for i in range(9):
            if tablero[i] == '-':
                tablero[i] = 'O'
                puntaje = minimax(tablero, False)
                tablero[i] = '-'
                mejor_puntaje = max(mejor_puntaje, puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = float('inf')
        for i in range(9):
            if tablero[i] == '-':
                tablero[i] = 'X'
                puntaje = minimax(tablero, True)
                tablero[i] = '-'
                mejor_puntaje = min(mejor_puntaje, puntaje)
        return mejor_puntaje
```

En este fragmento de código, si es el turno de la computadora, el algoritmo busca maximizar el valor del estado resultante (`mejor_puntaje`). Si es el turno del jugador humano, se busca minimizar dicho valor. La recursión continúa hasta que se alcanza un estado terminal (victoria, derrota o empate).

### Función: `mejor_movimiento_computadora(tablero)`

Esta función utiliza el algoritmo **Minimax** para encontrar la mejor jugada posible para la computadora. Recorre todas las celdas disponibles en el tablero y simula el resultado de colocar una **O** en cada una de ellas. Luego, evalúa el puntaje de cada posible jugada usando **Minimax** y selecciona la jugada que da el mejor puntaje para la computadora.

El código para seleccionar la mejor jugada es el siguiente:

```python
def mejor_movimiento_computadora(tablero):
    mejor_puntaje = -float('inf')
    mejor_movida = None
    for i in range(9):
        if tablero[i] == '-':
            tablero[i] = 'O'
            puntaje = minimax(tablero, False)
            tablero[i] = '-'
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movida = i
    return mejor_movida
```

La función recorre cada celda vacía, simula la jugada, y calcula el puntaje de esa jugada utilizando **Minimax**. Luego, elige la jugada con el puntaje más alto.

### Función Principal: `jugar_tic_tac_toe()`

Esta es la función que controla el flujo del juego. Primero, solicita al usuario que elija quién juega primero: el jugador humano (con **X**) o la computadora (con **O**). Dependiendo de la elección, alterna entre el jugador humano y la computadora. 

Cada turno, el tablero se imprime en la terminal, y después de cada jugada se verifica si hay un ganador utilizando la función `verificar_ganador`. Si se detecta un ganador, el juego termina y se muestra un mensaje en la terminal. Si el tablero se llena sin que haya un ganador, se declara empate.

### Ejecución del Juego

El juego se ejecuta utilizando un bloque `if __name__ == '__main__'`, que llama a la función `jugar_tic_tac_toe` para comenzar el juego. Esto permite que el juego sea ejecutado directamente desde la terminal.

## Código completo:

```python
import random
from colorama import Fore, Style, init

# Inicializar Colorama
init(autoreset=True)

# Función para imprimir el tablero con colores
def mostrar_tablero(tablero):
    print(Fore.YELLOW + "\nTablero actual:")
    for fila in range(0, 9, 3):
        print(Fore.YELLOW + "---|---|---")
        print(f" {mostrar_celda(tablero[fila])} | {mostrar_celda(tablero[fila+1])} | {mostrar_celda(tablero[fila+2])} ")
    print(Fore.YELLOW + "---|---|---\n")

# Función para mostrar cada celda con su respectivo color
def mostrar_celda(celda):
    if celda == 'X':
        return Fore.RED + 'X'
    elif celda == 'O':
        return Fore.GREEN + 'O'
    else:
        return celda

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

# Función para verificar si el tablero está lleno
def tablero_lleno(tablero):
    return '-' not in tablero

# Algoritmo Minimax para hacer que la computadora juegue de manera óptima
def minimax(tablero, es_maximizar):
    # Verificar si hay un ganador
    if verificar_ganador(tablero, 'O'):
        return 1  # Gana la computadora
    if verificar_ganador(tablero, 'X'):
        return -1  # Gana el jugador humano
    if tablero_lleno(tablero):
        return 0  # Empate

    if es_maximizar:
        mejor_puntaje = -float('inf')
        for i in range(9):
            if tablero[i] == '-':
                tablero[i] = 'O'
                puntaje = minimax(tablero, False)
                tablero[i] = '-'
                mejor_puntaje = max(mejor_puntaje, puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = float('inf')
        for i in range(9):
            if tablero[i] == '-':
                tablero[i] = 'X'
                puntaje = minimax(tablero, True)
                tablero[i] = '-'
                mejor_puntaje = min(mejor_puntaje, puntaje)
        return mejor_puntaje

# Función para encontrar el mejor movimiento de la computadora
def mejor_movimiento_computadora(tablero):
    mejor_puntaje = -float('inf')
    mejor_movida = None
    for i in range(9):
        if tablero[i] == '-':
            tablero[i] = 'O'
            puntaje = minimax(tablero, False)
            tablero[i] = '-'
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movida = i
    return mejor_movida

# Función principal del juego
def jugar_tic_tac_toe():
    tablero = ['-'] * 9
    jugador = input(Fore.YELLOW + "¿Quién juega primero? (X para usuario, O para computadora): ").upper()

    while jugador not in ['X', 'O']:
        jugador = input(Fore.YELLOW + "Opción inválida. Elige X (usuario) o O (computadora): ").upper()

    turno_actual = 'X' if jugador == 'X' else 'O'
    
    while True:
        mostrar_tablero(tablero)
        
        # Movimiento del jugador actual
        if turno_actual == 'X':
            movimiento_valido = False
            while not movimiento_valido:
                try:
                    movida = int(input(Fore.YELLOW + "Elige una posición (1-9): ")) - 1
                    if tablero[movida] == '-':
                        tablero[movida] = 'X'
                        movimiento_valido = True
                    else:
                        print(Fore.YELLOW + "Posición ocupada, elige otra.")
                except (ValueError, IndexError):
                    print(Fore.YELLOW + "Entrada inválida, elige una posición entre 1 y 9.")
        else:
            print(Fore.YELLOW + "Turno de la computadora...")
            movida = mejor_movimiento_computadora(tablero)
            tablero[movida] = 'O'

        # Verificar si hay un ganador
        if verificar_ganador(tablero, turno_actual):
            mostrar_tablero(tablero)
            if turno_actual == 'X':
                print(Fore.RED + "¡Felicidades, ganaste!")
            else:
                print(Fore.GREEN + "La computadora ha ganado.")
            break

        # Verificar si el tablero está lleno
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print(Fore.YELLOW + "El juego termina en empate.")
            break

        # Cambiar de turno
        turno_actual = 'O' if turno_actual == 'X' else 'X'

# Ejecutar el juego
if __name__ == '__main__':
    jugar_tic_tac_toe()
```

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

## Examen
1. [Introducción](#Introducción)
2. [Código_ejercicio1](#Código_ejercicio1)
3. [Código_ejercicio2](#Código_ejercicio2)
***


<h1 align="center">1.Introducción</h1>

<B>Este es el link del [Repositorio](https://github.com/Diegodesantos1/Examen)</B>

*He realizado los 2 ejercicios del examen, el primero te cuenta vocaes y consonantes a una palabra dada y el segundo es un juego de ajedrez con unas normas especícas en las que solo puedes mover las torres en vertical, es decir en el eje y o el eje de abscisas*
***

<h1 align="center">2.Código_ejercicio1</h1>
```python
# Ejercicio del minion


def juego(string):
    ListaVocales = [
        "a",
        "e",
        "i",
        "o",
        "u",
        "A",
        "E",
        "I",
        "O",
        "U",
    ]  # Tanto mayúsculas como minúsculas
    consonantes = 0
    vocales = 0
    nombrejugador2 = "Stuart"
    nombrejugador1 = "Kevin"
    print(f"El nombre del jugador 1 es {nombrejugador1}")
    print(f"El nombre del jugador 2 es {nombrejugador2}")
    numpalabras = len(string)
    for i, j in enumerate(string):
        if j in ListaVocales:
            vocales += numpalabras - i
        else:
            consonantes += numpalabras - i
    if vocales == consonantes:
        print("Han empatado Stuart y Kevin")
    elif vocales < consonantes:
        print("Ha ganado Stuart con {} puntos".format(consonantes))
    else:
        print("Ha ganado Kevin con {} puntos".format(consonantes))


print("¿Con que palabra quieres jugar?")
palabra_jugar = str(input())  # Creo la variable palabra para así jugar con ella
juego(palabra_jugar)  # La pongo en la función
```
***
<h1 align="center">2.Código_ejercicio2</h1>
```python
# Ejercicio de las torres
# T = Número de juegos a jugar, N= tamaño del tablero
def jugar_ajedrez():
    print("Escriba el nombre del primer jugador")
    nombrejugador1 = str(input())
    print("Escriba el nombre del segundo jugador")
    nombrejugador2 = str(input())
    print("¿Cuántos juegos quieres jugar?")
    T = int(input())
    if 1 <= T <= 10:
        print("Número válido, seguimos")
    else:
        print("Número NO válido,")
        print("¿Cuántos juegos quieres jugar?")
        T = int(input())
    print("De qué tamaño quieres el tablero")
    N = int(input())
    if 2 <= N <= 2000:
        print(
            "Número válido, seguimos, ahora debes pulsar el número que acabas de poner tantas veces como turnos posibles tiene el tablero"
        )
    else:
        print("Número NO válido,")
        print("De qué tamaño quieres el tablero")
        N = int(input())
    for i in range(T):
        jugador1 = [
            int(input()) - 1 for i in range(N)
        ]  # Establezco el bucle para que se muevan las piezas en el rango del tamaño del tablero
        jugador2 = [int(input()) - 1 for i in range(N)]

    movimientos = 0
    for i in range(N):
        distanciamovimiento = abs(
            jugador1[i] - jugador2[i]
        )  # Solo se mueven las piezas en el eje de abcisas, por eso el abs, solo se mueven en vertical
        movimientos ^= distanciamovimiento - 1  # Se eleve la solución
    if movimientos != 0:
        jugador1 = nombrejugador1
        print(
            "Ha ganado", jugador1
        )  # Ya que el que empieza es el jugador 1, por lo que si se queda sin movmientos, se acaba el juego
    else:
        jugador2 = nombrejugador2
        print("Ha ganado", jugador2)


jugar_ajedrez()


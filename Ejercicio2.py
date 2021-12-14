#Ejercicio de las torres
#T = Número de juegos a jugar, N= tamaño del tablero
print("Escriba el nombre del primer jugador")

print("¿Cuántos juegos quieres jugar?")
T = int(input())
if 1 <= T <= 10:
    print("Número válido, seguimos")
else:
    print("Número NO válido,")
    print("¿Cuántos juegos quieres jugar?")
    T = int(input())
print("De qué tamaño quieres el tablero")
N=int(input())
if 2 <= N <= 2000:
    print("Número válido, seguimos")
else:
    print("Número NO válido,")
    print("De qué tamaño quieres el tablero")
    N = int(input())
for i in range(T):
    jugador1 = [int(input())-1 for i in range(N)] #Establezco el bucle para que se muevan las piezas en el rango del tamaño del tablero
    jugador2 = [int(input())-1 for i in range(N)]

movimientos = 0
for i in range(N):
    distanciamovimiento = abs(jugador1[i] - jugador2[i]) #Solo se mueven las piezas en el eje de abcisas, por eso el abs, solo se mueven en vertical
    movimientos **= (distanciamovimiento - 1) #Se eleve la solución

if movimientos != 0:
    print("Ha ganado el jugador 2") #Ya que el que empieza es el jugador 1, por lo que si se queda sin movmientos, se acaba el juego
else:
    print("Ha ganado el jugador 1")
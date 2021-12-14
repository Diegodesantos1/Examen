#Ejercicio de las torres
#T = Número de juegos a jugar, N= tamaño del tablero
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

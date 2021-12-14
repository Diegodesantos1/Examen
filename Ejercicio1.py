#Ejercicio del minion

def juego(string):
    ListaVocales=['a','e','i','o','u','A','E','I','O','U'] #Tanto mayúsculas como minúsculas
    consonantes = 0
    vocales = 0
    nombrejugador2= "Stuart"
    nombrejugador1= "Kevin"
    print(f"El nombre del jugador 1 es {nombrejugador1}")
    print(f"El nombre del jugador 2 es {nombrejugador2}")
    numpalabras= len(string)
    for i, j in enumerate(string):
        if j in ListaVocales:
            vocales += numpalabras - i
        else:
            consonantes += numpalabras - i
    if vocales == consonantes:
        print("Han empatado Stuart y Kevin")
    elif vocales < consonantes:
        print("Ha ganado Stuart")
    else:
        print ("Ha ganado Kevin")

print("¿Con que palabra quieres jugar?")
palabra_jugar=str(input()) #Creo la variable palabra para así jugar con ella
juego(palabra_jugar) #La pongo en la función

# Creando un diccionario para representar un jugador
jugador = {
    "posicion": "delantero",
    "nacionalidad": "brasil",
    "edad": 25,
    "valor": 50000000,
    "equipo": "psv",
    "goles": 35,
}

# Accediendo a los datos usando las llaves
print("---Información del jugador")
print("posición:", jugador["posicion"])
print("edad", jugador["edad"])
print("equipo", jugador["equipo"])
print("goles", jugador["goles"])

# Podemos usar un if con los datos del diccionario

if jugador["valor"] < 55000000 and jugador["goles"] > 25:
    print("El jugador es de " + jugador["nacionalidad"] + " anotó " + str(jugador["goles"]) + " goles")
else:
    print("No es o que estamos buscando")
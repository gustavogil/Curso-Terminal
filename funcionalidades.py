import random

# El programa elige un número secreto entre 1 y 100
numero_secreto = random.randint(1, 100)

# Damos la bienvenida al jugador
print("Bienvenido al juego Número Secreto, donde deberás atinarle al número secreto en el menor número de oportundiades posible!")

# Pedimos el primer número
numero = int(input("Elige un número entre 1 y 100: "))

# Se compara el primer número con el número secreto y empieza el bucle // recordar que si ya hay un if, los siguientes son elif
while numero != numero_secreto:
    if numero > numero_secreto:
        print("Uff, te pasaste, elige un nuevo número entre 1 y 100")
    elif numero < numero_secreto:
        print("Uff, te quedaste corto, elige un nuevo número entre 1 y 100")
    
    # Pedimos el siguiente intento
    numero = int(input("Elige un nuevo número entre 1 y 100: "))

print("Lo lograste champ. has ganado")
    

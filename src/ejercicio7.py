import random

def juego_adivina_numero(maximo):
    numero_secreto = random.randint(1,maximo)
    numero_intentos = 1
    vidas = int(input("¿Cuántas vidas desea tener?(entre 10 y 3): "))
    while vidas < 3 or vidas > 10:
        print('No te flipes, elije entre 10 y 3 vidas.')
        vidas = int(input("¿Cuántas vidas desea tener?(entre 10 y 3): "))
    sigue_jugando = True
    while sigue_jugando:
        if vidas == -1:
            print("Perdiste")
            break

        numero = int(input("Adivina el número: "))

        if numero_secreto < numero:
            print("El número secreto es MENOR")
            print(f"Te quedan {vidas} vidas")

        elif numero_secreto > numero:
            print("El número secreto es MAYOR")
            print(f"Te quedan {vidas} vidas")

        else:
            print("¡Acertaste!")
            sigue_jugando = False
            print("Has tardado", numero_intentos, "intentos")
        numero_intentos += 1
        vidas -= 1
        
            

juego_adivina_numero(100)
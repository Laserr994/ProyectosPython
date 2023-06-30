import random
import time

def mostrar_introduccion():
    print("Estas en una tierra de dragones, frente de ti.")
    print("hay dos cuevas, en una de ellas... el dragon será generoso y")
    print("amigable y compartirá su tesoro contigo.")
    print("mientras que el otro dragón es codicioso, esta hambiento y te devorará inmediatamente")
    print()

def elegir_cueva():
    cueva = ""
    while cueva != '1' and cueva != "2":
        print("a que cueva quieres ir? (1 o 2?)")
        cueva = input()
        
        return cueva
    
def explorar_cueva(cueva_elegida):
    print("Te aproximas a la cueva....")
    time.sleep(2)
    print("Es oscura y espeluznante...")
    time.sleep(2)
    print("¡Un gran dragón aparece súbitamente frente de ti!, abre sus fauces.")
    print()
    time.sleep(2)

    cueva_amigable = random.randint(1,2)

    if cueva_elegida == str(cueva_amigable):
        print("¡Te regala su tesoro!")
    else:
        print("¡te engulle de un bocado!")

jugar_de_vuelta = "si"
while jugar_de_vuelta == "si" or jugar_de_vuelta == "s":

    mostrar_introduccion()

    numero_cueva = elegir_cueva()

    explorar_cueva(numero_cueva)

    print("quieres jugar de nuevo? (si o no?)")
    jugar_de_vuelta = input()

else:
    print("nos vemos!")
    time.sleep(2)

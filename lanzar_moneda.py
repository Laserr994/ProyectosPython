#LanzarMoneda, en cual lanzará una moneda 1000 veces y adivinas cuantas veces caerá cara
#Presionando ENTER para comenzar el juego...
import random


print("Lanzaré una moneda 1000 veces. adivina cuantas veces caerá cara. (Presiona ENTER para comenzar...)")
input()

lanzamientos = 0
caras = 0 

while lanzamientos < 1000: #mientras que la variable lanzamientos es menor que 1000:
    if random.randint(0,1) == 1:
        caras = caras + 1
    lanzamientos = lanzamientos + 1

    if lanzamientos == 900:
        print("900 lanzamientos y hubo " + str(caras) + ' caras!')
    
    if lanzamientos == 500:
        print("la mitad de los lanzamientos y cara salió " + str(caras) + " veces-")

    if lanzamientos == 100:
        print("De 100 lanzamientos y hubo" + " " + str(caras) + " veces-")

print()
print("De 1000 lanzamientos, al final cara salió " + " " + str(caras) + " veces!")
print("¿Estuviste cerca?")

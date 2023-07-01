#ProyectoPython, Adivina el numero
import random

intentos_realizados = 0 

print("Hola!, como te llamas?...")
mi_nombre = input()

numero = random.randint(1,20)
print("bueno, " + mi_nombre + ", estoy pensando en un numero entre 1 y 20.")

while intentos_realizados < 6:
    print("intenta de adivinar.")
    estimación = input()
    estimación = int(estimación)

    intentos_realizados = intentos_realizados + 1

    if estimación < numero:
        print("tu estimación es muy baja, intenta de nuevo...")
    
    if estimación > numero:
        print("tu estimación es muy alta, intenta de nuevo...")
    
    if estimación == numero:
        break

if estimación == numero:
    intentos_realizados = str(intentos_realizados)
    print("buen trabajo, " + mi_nombre + " ! " + "has adivinado mi número en " + intentos_realizados + " intentos!")

if estimación != numero:
    numero = str(numero)
    print("Pues no, el numero que estaba pensando era " + numero)
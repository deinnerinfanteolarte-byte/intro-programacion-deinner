"""
Ejemplo:
El programa genera un numero al azar y el usuario intentará adivinarlo.
En cada intento, el programa le dirá si el numero a adivinar es mayor o menor.
El programa se acaba cuando la persona logre adivinar el número.
El programa mostrará cuantos intentos necesito el usuario para adivinar.
Gana la persona que adivine con menos intentos.
El numero al azar está entre 0 y 1000.
"""
 
import random

NUM_ADIVINAR = random. randint(0, 100)

intentos = 0
while True:
    # Leer y validar el numero del usuario
    num = 0
    while True:
        num = int(input("intente adivinar.ingres un numero de 0 a 1000 "))
        if 0 <= num <= 1000:
           break
        print("==> Eror numero invalio. el rango es de 0 a 1000. ")
        input("presione enter para continuar ... ")
        print("")

    if num == NUM_ADIVINAR:
           break
    if num > NUM_ADIVINAR: #900 600
        input("el numero a adivinar es mayor. \npresiones enter para continuar ...")
        print("")
    else: #600 850
        input("el numero a adivinar es mayor. \npresiones enter para continuar ...")
        print("")

print("haz adivinar!!!")
print("uso ", intentos, " intento(s).")
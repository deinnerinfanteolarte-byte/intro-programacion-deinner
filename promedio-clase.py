"""
Ejemplo:
un prosefor necesita crear un programa que le ayude a calcular el promedio de notas de un salon de clases
El ingresa el nombre y el valor de nota final de cada estudiante.
Al final necesita saber cual es el mejor estudiante y el promedio de todo el curso.
"""


cantidad_est = int(input("cantidad de estudiante? "))

mejor_est = ""
nota_mayor = 0.0
suna = 0.0
promedio = 0.0

for veces in range (1, cantidad_est+1):
    print("estudiante #", veces)
    nombre = input("Nombre ")
    nota = float(input("nota? "))

    suma = suma + nota #<- Acumuladores

    if nota > nota_mayor: #Encontar el estudiante con mayor nota
    nota_mayor = nota
    mejor_est = nombre

promedio = suna / cantidad_est

print("el promedio del curso es: ", promedio)
print("el mejor estudiante es: ", mejor_est, "con nota de:", nota_mayor)
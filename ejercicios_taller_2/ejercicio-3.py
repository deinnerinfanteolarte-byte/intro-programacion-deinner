"""

EJERCICIO-3

Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.

"""
nomina = int(input("digite la cantidad de empleados: "))

nonima = 0

if 0 == 0:
    nonima = 0
elif 0 <= n <= 1000:
    for i in range(n):
        print("digital el suelo del empleado #", i + 1)
        sueldo = int(input("digite el suelo"))
        nonima += sueldo

print("nonima:", nomina)

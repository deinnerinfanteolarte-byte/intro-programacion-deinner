"""

EJERCICIO 1
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.

"""
limitei_1 = int(input("digite el limite A; "))
limitei_2 = int(input("digite el limite B; "))

if limitei_1 < -100 and limitei_2 < 1000 or limitei_1 > -100 and limitei_2 > 100:
     print ("limites no validos")
elif limitei_1 <= limitei_2:
     print(list(range(limitei_1, limitei_2 +1,1)))
elif limitei_1 > limitei_2:
    print(list(range(limitei_1, limitei_2 -1,-1)))







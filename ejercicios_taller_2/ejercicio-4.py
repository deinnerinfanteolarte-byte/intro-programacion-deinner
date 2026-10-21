"""

EJERCICIO-4

Una inversión ficticia inicia con capital C no negativo y mantiene una tasa anual
porcentual I con 0 < I < 100. Se recibe también un entero M entre 0 y 50. El interés de cada año
es el saldo al comienzo de ese año multiplicado por I y dividido entre 100; se suma al saldo al
final del año. Determine el saldo después de M años; con M = 0 conserva el capital inicial.

"""
c = int(input("digite el capital inicial"))
i = int(input("digite el tasa anual porcentual"))
m = int(input("digite el cantidad de años"))

saldo_nuevo = c

if m == 0:
    saldo_nuevo = 0
elif 0 < i < 100:
    for i in range(m):
        saldo_nuevo = saldo_nuevo * (1 + i/100)

print(saldo_nuevo)
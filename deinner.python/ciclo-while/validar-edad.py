"""
Ejemplo un promama que lea una de camper y continue si esta es valida.
una edad es: 16 <= edad_camper <= 40}

"""

edad = int(input("edad? "))
while True:
    if edad < 16 or edad > 40:
        print("error. edad invalidad. vuelva a ingresar" [16, 40].")
        input("prediose cualquier tecla para continuar ::: ")
        edad = int(input("\nedad? "))
    else: 
        print("\nEdad correcta.")
        break
            
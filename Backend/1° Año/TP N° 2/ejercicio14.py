"""14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
no es bisiesto
"""
#Definimos la función
def año_bisiesto(añoUsuario):
    #Creamos la estructura de control
    if (añoUsuario % 4 == 0 and añoUsuario % 100 != 0) or (añoUsuario % 400 == 0):
        return True
    else:
        return False
#Solicitamos el ingreso del año al usuario
añoUsuario = int(input('Ingresa un año: '))
#Realizamos las validaciones
if año_bisiesto(añoUsuario):
    print(f'{añoUsuario} es bisiesto')
else:
    print(f'{añoUsuario} no es bisiesto')
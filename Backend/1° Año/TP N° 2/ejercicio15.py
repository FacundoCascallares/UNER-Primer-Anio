"""15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
informarle que no se puede procesar el dato
"""
#Definimos la función con un metodo lower()
def letraUsuario(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if letra.lower() in vocales:
        return True
    else:
        return False
#Solicitamos al usuario que ingrese una letra
letra = input('Ingresa una letra: ')
if len(letra) != 1:
    print('¡¡¡Error!!! Debes ingresar solo un carácter.')
#El metodo isalpha comprueba si la letra ingresada es un caracter de la A a la Z
elif not letra.isalpha():
    print('¡¡¡Error!!'' Debes ingresar una letra validad.')
elif letraUsuario(letra):
    print('Es vocal.')
else:
    print('No es vocal.')
"""13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
el grupo que le corresponde
"""
#Definimos la función
def determinar_grupo(nombre, sexo):
    grupo = ""
    #Creamos la estructura de control con una función lower()
    if sexo.lower() == 'femenino':
        if nombre.lower() < 'm':
            grupo = 'A'
        else:
            grupo = 'B'
    elif sexo.lower() == 'masculino':
        if nombre.lower() > 'n':
            grupo = 'A'
        else:
            grupo = 'B'
    else:
        print('Sexo no válido')
        return

    print(f'El grupo al que perteneces es: {grupo}')
#Solicitamos al usuario que ingrese su sexo y su nombre
nombreUsuario = input('Ingrese su nombre: ')
sexoUsuario = input('Ingrese sexo (Masculino/Femenino): ')

determinar_grupo(nombreUsuario, sexoUsuario)
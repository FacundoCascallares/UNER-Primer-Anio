#1. Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!

def nombre(nombre):
    print(f'¡Hola {nombre}!')

#Solicitamos el nombre al usuario
nombre2 = input('Ingrese su nombre:')
print(nombre(nombre2))
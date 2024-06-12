"""10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
a. Todoslos números impares desde 1 hasta ese número separados por comas.
b. La cuenta atrás desde ese número hasta cero separados por comas.
c. Que indique si es primo o no.
d. Por último,su factorial"""

numero = int(input('Ingrese un número entero positivo: '))

#A Muestra los números impares
numeros_lista = []
for i in range(1, numero, 2):
    numeros_lista.append(str(i))
print(F'Ejercicio A: {numeros_lista}')

#B Realiza el conteo hacia atras
numeros_lista = []
for i in range(numero, 0, -1):
    numeros_lista.append(str(i))
print(f'Ejercicio B: {numeros_lista}')

#C Define si un número es primo o no, me costo bastante la logica
def num_primo(numero):
    if numero <=1:
        return False
    for i in range(2, int(numero ** 0.5) +1):
        if numero % 1 == 0:
            return False
    return True
if num_primo(numero):
    print(f'Ejercicio C: El número {numero} es primo.')
else:
    print(f'Ejercicio C: El número {numero} no es primo.')

#D Buscamos el factorial del número ingresado por el usuario, este me costo mucho
def factorial(numero):
    if numero == 0:
        return 1
    fact = 1
    for i in range(1, numero + 1):
        fact *= i
    return fact
print(f'Ejercicio D: El factorial de {numero} es {factorial(numero)}.')
#4. Que dada la base y altura de un triángulo nos calcule su área.

#Definimos la función
def area(base, altura):
    print(f'La base del triángulo es: {base}')
    print(f'La altura del triangulo es: {altura}')
    #Esta es la operación a realizar
    return base * altura

#Solicitamos al usuario que ingrese las medidas del triangulo
base1 = int(input("Ingrese la base del triángulo: "))
altura1 = int(input("Ingrese la altura del triángulo: "))

resultado = area(base1, altura1)

print(f'El area del triángulo es: {resultado}')
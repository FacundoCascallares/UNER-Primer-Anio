#5. Que dado tres números ingresados por el usuario nos devuelva el promedio
def promedio(valor1, valor2, valor3):
     suma = valor1 + valor2 + valor3
     #Operación matematica a realizar
     return suma / 3
#Le solicitamos al usuario que ingrese los valores
suma1 = int(input('Ingrese el primer valor: '))
suma2 = int(input('Ingrese el segundo valor: '))
suma3 = int(input('Ingrese el tercar valor: '))

print(f'Los numeros ingresados son: {suma1}, {suma2}, {suma3}')
print(f'El promedio es: {promedio(suma1, suma2, suma3)}')


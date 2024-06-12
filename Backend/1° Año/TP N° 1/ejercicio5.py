"""Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
forma: “La respuesta es XX”."""

num1 = int(input("Ingrese el primer valor a sumar: "))
num2 = int(input("Ingrese el segundo valor a sumar: "))
num3 = int(input("Ingrese el valor por el cual va a multiplicar la suma: "))

suma = num1 + num2
multiplicacion = suma * num3

print(f'La respuesta es: {multiplicacion}')
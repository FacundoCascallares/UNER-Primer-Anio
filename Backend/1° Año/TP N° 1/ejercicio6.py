"""Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
número de comensales y mostrar cuánto debe pagar cada persona."""

totalCuenta = int(input("Ingrese el total de la cuenta: "))
comensales = int(input("Ingrese la cantidad de comensales: "))
totalPorComensal = totalCuenta / comensales

print(f'El total de la cuenta es: {totalCuenta}, el total a abonar por {comensales} comensales es: {totalPorComensal}')
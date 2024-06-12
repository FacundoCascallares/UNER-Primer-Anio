"""Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
segundos son esos números de días"""
dias = int(input("Ingrese la cantidad de días: "))

diasHora = dias * 24
diasMinutos = dias * (24 * 60)
diasSegundos = dias * (24 * (60 * 60))

print(f'En {dias} dias usted dispone de: {diasHora} horas, {diasMinutos} minutos, {diasSegundos} segundos.')
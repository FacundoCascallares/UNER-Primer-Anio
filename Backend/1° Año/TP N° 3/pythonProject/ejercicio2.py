#Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
#Imprimir por pantalla el resultado.

# Inicializar una lista vacía para almacenar los números
numeros = []

#Con la función range generamos 5 pedidos de ingreso de número al usuario
for i in range(5):
    while True:
        try:
            numeroUsuario = int(input("Ingrese un número: "))
            numeros.append(numeroUsuario)
            break
        except ValueError:
            print("Ingrese un número válido.")
#El metodo sort() ordena la lista
numeros.sort()

print("Números ingresados y ordenados:", numeros)

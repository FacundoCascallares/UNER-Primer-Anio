#Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
#usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
#de los números ingresados por el usuario deberá ser almacenado en una lista. A
#continuación, realice las siguientes tareas:
#a. Determinar el máximo.
#b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#c. Determinar el mínimo.
#d. Calcular la multiplicación de todos los números de la lista.
#e. Contar los valores pares e impares.
#f. Remover los elementos repetidos.

def solicitarNumeros():
    numeros = []
    while True:
        entrada = input("Ingrese un número entero (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    return numeros

#A - Determinar el máximo.
def determinarMaximo(numeros):
    return max(numeros)

#B - Obtener segundo valor máximo. Es decir el que le sigue al máximo.
def obtenerSegundoMaximo(numeros):
    maximo = max(numeros)
    numerosSinMaximo = [num for num in numeros if num != maximo]
    if numerosSinMaximo:
        segundoMaximo = max(numerosSinMaximo)
        return segundoMaximo
    else:
        return None

#C - Determinar el mínimo.
def determinarMinimo(numeros):
    return min(numeros)

#D - Calcular la multiplicación de todos los números de la lista.
def multiplicacionLista(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

#E - Contar los valores pares e impares.
def contarParesImpares(numeros):
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = sum(1 for num in numeros if num % 2 != 0)
    return pares, impares

#F - Remover los elementos repetidos.
def removerRepetidos(numeros):
    return list(set(numeros))

def main():
    numeros = solicitarNumeros()
    if numeros:
        maximo = determinarMaximo(numeros)
        segundoMaximo = obtenerSegundoMaximo(numeros)
        minimo = determinarMinimo(numeros)
        multiplicacion = multiplicacionLista(numeros)
        pares, impares = contarParesImpares(numeros)
        numeros_unicos = removerRepetidos(numeros)

        print(f'Los números ingresados son: {numeros}')
        print(f'El número más alto ingresado es: {maximo}')
        if segundoMaximo is not None:
            print(f'El segundo número más alto ingresado es: {segundoMaximo}')
        else:
            print('No hay segundo máximo ya que todos los números son iguales.')
        print(f'El número mínimo ingresado es: {minimo}')
        print(f'La multiplicación de todos los números es: {multiplicacion}')
        print(f'Números de valores pares: {pares}')
        print(f'Números de valores impares: {impares}')
        print(f'Lista sin números repetidos: {numeros_unicos}')
    else:
        print('No se ingresaron números.')

if __name__ == "__main__":
    main()

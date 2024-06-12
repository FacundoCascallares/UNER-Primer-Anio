#17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.
#Creamos la función para ver si un número es primo o no
def numero_primo(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos_hasta_100():
    primos = []
    for num in range(101):
        if numero_primo(num):
            primos.append(num)
    return primos

primos_en_rango = numeros_primos_hasta_100()
cantidad_primos = len(primos_en_rango)

print('Los números primos entre 0 y 100 son:')
for primo in primos_en_rango:
    print(primo, end=" ")
print('\nCantidad de números primos:', cantidad_primos)
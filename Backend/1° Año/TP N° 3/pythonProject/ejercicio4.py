#Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
#realizar lo siguiente:
#a. Imprimir la cantidad de elementos que tiene la lista.
#b. Imprimir el primer y último elemento.
#c. Imprimir el resto.
#d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
#la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
#e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
#la lista. Quitar el elemento correspondiente de esa posición.
#f. Imprimir la lista en orden inverso.
#g. Vaciar la lista

paises = ['Argentina','Brasil', 'Bolivia','Paraguay','Venezuela']

#A - Imprimir la cantidad de elementos que tiene la lista.

print(f'Cantidad de elementos de la lista: ',len(paises))

#B- Imprimir el primer y último elemento.
print(f'Primer Elemento: ', paises[0])
print(f'Ultimo Elemento: ', paises[4])

#C - Imprimir el resto.
print(paises[1:4])

#D - Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
#la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.

paisUsuario = input('Ingrese el nombre de un país para buscar en la lista: ').strip().capitalize()
if paisUsuario in paises:
    print(f"El país '{paisUsuario}' se encuentra en la lista en la posición {paises.index(paisUsuario)}.")
else:
    print(f"El país '{paisUsuario}' no se encuentra en la lista.")

#E - Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
#la lista. Quitar el elemento correspondiente de esa posición.

while True:
    try:
        numeroPosicion = int(input(f"Ingrese un número entre 0 y {len(paises)-1} para eliminar el elemento correspondiente: "))
        if 0 <= numeroPosicion < len(paises):
            eliminado = paises.pop(numeroPosicion)
            print(f"Se ha eliminado el país: {eliminado}")
            break
        else:
            print(f"Por favor, ingrese un número válido entre 0 y {len(paises)-1}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

#F - Imprimir la lista en orden inverso.
print("Lista en orden inverso:", paises[::-1])

#g - Vaciar la lista.
paises.clear()
print("Lista vacía:", paises)
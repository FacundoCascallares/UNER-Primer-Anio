#Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
#de una lista vacía:
#a. Agregar un elemento al final.
#b. Agregar un elemento al principio.
#c. Quitar un elemento al final.
#d. Quitar un elemento al principio

#Definimos las opciones del menu
def menu():
    print("\nMenú de opciones:")
    print('1. Agregar un elemento al final')
    print('2. Agregar un elemento al principio')
    print('3. Quitar un elemento al final')
    print('4. Quitar un elemento al principio')
    print('5. Mostrar lista')
    print('6. Salir')

def agregarAlFinal(lista):
    elemento = input('Ingrese el elemento a agregar al final: ')
    lista.append(elemento)
    print(f"Elemento '{elemento}' agregado al final.")

def agregarAlPrincipio(lista):
    elemento = input('Ingrese el elemento a agregar al principio: ')
    lista.insert(0, elemento)
    print(f"Elemento '{elemento}' agregado al principio.")

def quitarAlFinal(lista):
    if lista:
        elemento = lista.pop()
        print(f"Elemento '{elemento}' quitado del final.")
    else:
        print('La lista está vacía. No hay elementos para quitar.')

def quitarAlPrincipio(lista):
    if lista:
        elemento = lista.pop(0)
        print(f"Elemento '{elemento}' quitado del principio.")
    else:
        print('La lista está vacía. No hay elementos para quitar.')

def mostrarLista(lista):
    print('Lista actual:', lista)

def main():
    lista = []
    while True:
        menu()
        opcion = input('Seleccione una opción: ')

        #Creamos el acceso al menu de opciones
        if opcion == "1":
            agregarAlFinal(lista)
        elif opcion == "2":
            agregarAlPrincipio(lista)
        elif opcion == "3":
            quitarAlFinal(lista)
        elif opcion == "4":
            quitarAlPrincipio(lista)
        elif opcion == "5":
            mostrarLista(lista)
        elif opcion == "6":
            print('Saliendo del programa.')
            break
        else:
            print('Opción no válida. Por favor, intente de nuevo.')

if __name__ == "__main__":
    main()

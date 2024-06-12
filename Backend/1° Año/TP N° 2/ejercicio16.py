"""16. Que imprima el siguiente patrón:
54321
4321
321
21
1
"""
#Creamos la función
def imprimir_patron(fila):
    for i in range(fila, 0, -1):
        for j in range(i, 0, -1):
            print(j, end='')
        print()

imprimir_patron(5)
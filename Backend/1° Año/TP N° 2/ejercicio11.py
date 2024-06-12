#11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
#encuentran en dicha frase.

#Creamos la función, con las vocales a contrar. Podría usar el metodo lower() para poner menos vocales
def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    for vocal in frase:
        #Usamos un contador
        if vocal in vocales:
            contador += 1
    return contador

frase = input("Ingrese una frase: ")

cantidad_vocales = contar_vocales(frase)

print(f"La cantidad de vocales en la frase es: {cantidad_vocales}")
"""Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
derecho que al revés. Por ejemplo: rayar, kayak, somos"""

texto = input("Ingrese el texto a verificar si es palindromo: ")

texto = texto.lower().replace(" ", "")

textoPalindromo = texto[::-1]

if textoPalindromo == texto:
    print(texto)
    print(textoPalindromo)
    print(f'El texto es palindromo.')
else:
    print("El texto no es palindromo.")
""". Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
1985 -> Usuario: mfrancisconi, Contraseña: mf.1985."""

apellido = input("Ingrese su apellido: ")
nombre = input("Ingrese su nombre: ")
añoNacimiento = int(input("Ingrese su año de nacimiento: "))

print(f'Usuario recomendado: {nombre[0:1].lower()}{apellido.lower()}, Contraseña Recomendada: {nombre[0:1].lower()}{apellido[0:1].lower()}{añoNacimiento}')
# Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
#frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
#debajo la misma lista pero sólo con las frutas que añadió el usuario

frutas = ['banana', 'manzana', 'pera']
frutasUsuario = []
#Con la función range generamos 3 pedidos de ingreso de frutas al usuario
for i in range(3):
    while True:
            frutaUsuario = input(f'Ingrese el nombre de una fruta, sin repetir las que ya están: ')
            #Si la fruta ingresada se encuentra en la lista, se le va a pedir al usuario que ingrese nuevamente
            #una fruta
            if frutaUsuario in frutas or frutaUsuario in frutasUsuario:
                print('La fruta ya  se encuentra en la lista. Por favor, agregue una fruta diferente')
            else:
                frutas.append(frutaUsuario)
                frutasUsuario.append(frutaUsuario)
                break
print(frutas)
print(frutasUsuario)
#2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.

def exponenciacion(numero, potencia):
    print(f'El número a potenciar es: {numero}')
    print(f'El número a potenciar es: {potencia}')
    #Operación matematica a realizar
    return numero ** potencia

#Solicitamos al usuario que ingrese los datos
numero1 = int(input('Ingrese el número a potenciar: '))
potenciador = int(input('Ingrese el número a potenciar: '))

resultado = exponenciacion(numero1, potenciador)
print(f'El resultado de {numero1} elevado a la potencia de {potenciador} es: {resultado}')
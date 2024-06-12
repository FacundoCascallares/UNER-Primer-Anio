#9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
#en que ambos números son iguales.

num1 = int(input('Ingrese un número para comparar:'))
num2 = int(input('Ingrese el segundo número para comparar: '))
#Comparamos los números
if num1 < num2:
    print(num1)
#Si los números ingresados son iguales, le solicitamos al usuario que ingrese números diferentes
elif num2 == num1:
    print('Los números son iguales. Por favor ingrese números diferentes para poder comparar.')
else:
    print(num2)
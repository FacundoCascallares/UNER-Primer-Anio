#8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input('Ingrese su edad: '))
#Condicional para determinar si el usuario es menor o mayor de edad.
if edad < 18:
    print(f'Su edad es {edad}, usted es menor.')
else:
    print(f'Su edad es {edad}, usted es mayor.')
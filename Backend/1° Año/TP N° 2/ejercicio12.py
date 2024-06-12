#12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
#mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
#ingresado no es ninguno de esos, imprimir otro mensaje.

dia = input('Ingrese un día de la semana: ')
#Realizamos una estructura de control. La variable dia va acompañada de la función lower() para no depender de que
#el usuario ingrese minusculas o mayusculas o mezcle las letras.
#Quizás haya un metodo más corto de hacer esto. Esta manera me resulto más facíl.
if dia.lower() == 'lunes':
    print('Hoy es lunes.')
elif dia.lower() == 'viernes':
    print('Hoy es viernes.')
elif dia.lower() == 'sabado' or dia.lower() == 'sábado':
    print('Hoy es sábado.')
elif dia.lower() == 'domingo':
    print('Hoy es domingo.')
else:
    print('¿Que día será hoy?')
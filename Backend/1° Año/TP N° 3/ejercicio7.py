#7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
#con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
#usuario:
#a. Agregar nuevas tareas pendientes.
#b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
#de la lista de pendientes a la de terminadas.
#Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
#listas.

#Definimos el menu de opciones
def Menu():
    print("\nMenú de opciones:")
    print('1. Agregar nueva tarea pendiente')
    print('2. Marcar tarea pendiente como terminada')
    print('3. Mostrar listas de tareas')
    print('4. Salir')


def agregarTareaPendiente(tareasPendientes):
    tarea = input('Ingrese una nueva tarea pendiente: ')
    tareasPendientes.append(tarea)
    print(f"Tarea '{tarea}' agregada a la lista de pendientes.")


def marcarTareaTerminada(tareasPendientes, tareasTerminadas):
    if not tareasPendientes:
        print('No hay tareas pendientes para marcar como terminadas.')
        return

    print('Lista de tareas pendientes:')
    for idx, tarea in enumerate(tareasPendientes, start=1):
        print(f"{idx}. {tarea}")

    try:
        numeroTarea = int(input('Ingrese el número de la tarea que desea marcar como terminada: '))
        if 1 <= numeroTarea <= len(tareasPendientes):
            tarea = tareasPendientes.pop(numeroTarea - 1)
            tareasTerminadas.append(tarea)
            print(f"Tarea '{tarea}' marcada como terminada.")
        else:
            print('Número de tarea inválido.')
    except ValueError:
        print('Por favor, ingrese un número válido.')


def mostrarListas(tareasPendientes, tareasTerminadas):
    print("\nTareas pendientes:")
    if tareasPendientes:
        for tarea in tareasPendientes:
            print(f"- {tarea}")
    else:
        print('No hay tareas pendientes.')

    print("\nTareas terminadas:")
    if tareasTerminadas:
        for tarea in tareasTerminadas:
            print(f"- {tarea}")
    else:
        print('No hay tareas terminadas.')


def main():
    tareasPendientes = []
    tareasTerminadas = []

    while True:
        Menu()
        opcion = input('Seleccione una opción: ')
        #Creamos el acceso al menu de opciones
        if opcion == "1":
            agregarTareaPendiente(tareasPendientes)
        elif opcion == "2":
            marcarTareaTerminada(tareasPendientes, tareasTerminadas)
        elif opcion == "3":
            mostrarListas(tareasPendientes, tareasTerminadas)
        elif opcion == "4":
            print('Saliendo del programa.')
            break
        else:
            print('Opción no válida. Por favor, intente de nuevo.')

        mostrarListas(tareasPendientes, tareasTerminadas)


if __name__ == "__main__":
    main()

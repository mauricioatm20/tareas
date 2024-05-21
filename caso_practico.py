class Tarea:
    def __init__(self, descripcion):
        """
        Inicializa una tarea con una descripción y un estado de completada (por defecto es False).
        """
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Devuelve una representación en cadena de la tarea, mostrando su descripción y estado.
        """
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"


class ListaDeTareas:
    def __init__(self):
        """
        Inicializa una lista vacía de tareas.
        """
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Crea una nueva tarea y la agrega a la lista.
        """
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_completada(self, posicion):
        """
        Marca una tarea como completada dada su posición en la lista.
        Maneja excepciones si la posición es inválida.
        """
        try:
            if 0 <= posicion < len(self.tareas):
                self.tareas[posicion].marcar_completada()
            else:
                raise IndexError("Posición fuera de rango.")
        except IndexError as e:
            print(f"Error: {e}")

    def mostrar_tareas(self):
        """
        Muestra todas las tareas con su estado.
        """
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")

    def eliminar_tarea(self, posicion):
        """
        Elimina una tarea de la lista dada su posición.
        Maneja excepciones si la posición es inválida.
        """
        try:
            if 0 <= posicion < len(self.tareas):
                self.tareas.pop(posicion)
            else:
                raise IndexError("Posición fuera de rango.")
        except IndexError as e:
            print(f"Error: {e}")


def menu():
    """
    Muestra un menú al usuario para realizar las diferentes operaciones sobre la lista de tareas.
    Permite agregar tareas, marcar tareas como completadas, mostrar todas las tareas, eliminar tareas y salir del programa.
    Maneja excepciones para entradas no válidas.
    """
    lista_de_tareas = ListaDeTareas()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la nueva tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                posicion = int(input("Número de la tarea a marcar como completada: ")) - 1
                lista_de_tareas.marcar_completada(posicion)
            except ValueError:
                print("Error: Debes ingresar un número entero.")
        elif opcion == "3":
            lista_de_tareas.mostrar_tareas()
        elif opcion == "4":
            try:
                posicion = int(input("Número de la tarea a eliminar: ")) - 1
                lista_de_tareas.eliminar_tarea(posicion)
            except ValueError:
                print("Error: Debes ingresar un número entero.")
        elif opcion == "5":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")


if __name__ == "__main__":
    menu()

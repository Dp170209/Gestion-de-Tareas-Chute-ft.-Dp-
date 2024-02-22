from tarea import Tarea
class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea): #funcion agregar tareas d:
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice_tarea):
        del self.tareas[indice_tarea]

    def obtener_reporte_de_tareas(self, completadas=False):
        tareas_a_reportar = [tarea for tarea in self.tareas if tarea.completada == completadas]
        return tareas_a_reportar

    def __str__(self):
        lista_de_tareas_str = "\n".join([f"{i + 1}. {tarea}" for i, tarea in enumerate(self.tareas)])
        return lista_de_tareas_str

    def guardar_tareas(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for tarea in self.tareas:
                archivo.write(f"{tarea.descripcion},{tarea.completada}\n")

    def cargar_tareas(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    descripcion, completada = linea.strip().split(',')
                    tarea = Tarea(descripcion)
                    tarea.completada = completada == 'True'
                    self.tareas.append(tarea)
        except FileNotFoundError:
            # Si el archivo no existe, no hay tareas que cargar
            pass

    

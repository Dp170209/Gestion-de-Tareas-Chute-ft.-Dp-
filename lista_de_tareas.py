class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice_tarea):
        del self.tareas[indice_tarea]

    def obtener_reporte_de_tareas(self, completadas=False):
        tareas_a_reportar = [tarea for tarea in self.tareas if tarea.completada == completadas]
        return tareas_a_reportar

    def __str__(self):
        lista_de_tareas_str = "\n".join([f"{i + 1}. {tarea}" for i, tarea in enumerate(self.tareas)])
        return lista_de_tareas_str

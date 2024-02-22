class Tarea:
    def __init__(self, descripcion): # :3
        self.descripcion = descripcion
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True

    def __str__(self):
        estado = "[x]" if self.completada else "[ ]"
        return f"{estado} {self.descripcion}"

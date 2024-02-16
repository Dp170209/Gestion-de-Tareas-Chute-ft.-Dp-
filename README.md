**Desarrollo de una Aplicacion de Lista de Tareas**

By: 
- Jared Pimentel aka **Dp**
- Franz Carvajal aka **MrBl4ck**

Crear una aplicación de lista de tareas que permita a los usuarios agregar las tareas, marcarlas como completadas, eliminarlas de la lista, generar reportes por estados de tareas en curso y tareas completadas.

La applicacion debe ser implementada utilizando un lenguaje de programación de su elección (por ejemplo, Python, Java o JavaScript) y debe incluir una interfaz de línea de comandos (CLI) para interectuar con ella (Menú de Opciones).

Se debe usar Programación Orientada a Objetos o Programación Modular o ambos.

**Planificación**
1. Planificación y diseño (16/02/2024) -> Dp y chute
2. Configuración del repositorio Git (16/02/2024) -> Dp y Chute
3. Creación de Ramas (18/02/2024) -> Chute
4. Desarrollo de funcionalidades (18/02/2024 - 20/02/2024) -> Dp y Chute
5. Revisión de código (20/02/2024) -> Dp y Chute
6. Pruebas y Depuración (20/02/2024) -> Dp y Chute
7. Documentación y Comentarios (21/02/2024) -> Dp
8. Finalización y Revisión (23/02/2024) -> Dp y Chute

**Diseño**
El diseño es simple con una salida por consola que dispondra de un menú de opciones que cumplirá con sus reséctivas funciones.

**Ramas**
- Rama principal (main o master): Rama donde se encuentra nuestra versión estable.
- Rama de desarrollo: Rama donde se agregaran las funciones trabajadas.
- Rama de funciones: Desarrollo de funciones nuevas.
- Rama de correción de errores: Rama donde se corregirán los posibles errores.

**Funciones**
_Agregar tareas_:
  - Solicitar al usuario que ingrese el nombre de la tarea.
  - Agregar la tarea a una lista en memoria.

_Marcar tareas como completadas:_
  - Mostrar la lista de tareas y permitir al usuario seleccionar una tarea por su número.
  - Cambiar el estado de la tarea seleccionada a "completada".

_Eliminar tareas:_
  - Mostrar la lista de tareas y permitir al usuario seleccionar una tarea por su número.
  - Eliminar la tarea seleccionada de la lista.

_Visualización de tareas:_
  - Mostrar todas las tareas en la lista, indicando su número, nombre y estado (completada o no).

_Filtrar tareas por estado:_
  - Permitir al usuario elegir entre ver todas las tareas, las tareas completadas o las tareas pendientes, mostrando solo las que correspondan al estado seleccionado.

_Generación de reportes:_
  - Contar el número de tareas completadas y pendientes, mostrando estos totales al usuario.

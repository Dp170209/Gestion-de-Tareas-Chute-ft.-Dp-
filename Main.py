import os
import sys, signal, pyfiglet

# Ctrl + C
signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(1))

tareas = []  # Lista para almacenar las tareas

def limpiar_pantalla():
    os.system('cls')

def mostrar_menu():
    print("1. Agregar Tarea")
    print("2. Marcar Tareas como Completadas")
    print("3. Eliminar Tarea")
    print("4. Visualizar tarea")
    print("5. Estado de Tarea")
    print("6. Reporte de Tarea")
    print("7. Salir")

def opcion_uno():
    limpiar_pantalla()
    Agregar.agregar_tarea(tareas)

def opcion_dos():
    limpiar_pantalla()
    print("Tareas:")
    if not tareas:
        print("[!] No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"Tarea {i}: {tarea['nombre']} - Estado: {'completa' if tarea['completa'] else 'incompleta'}")
        opcion = input("Ingrese el número de la tarea que desea marcar como completa: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(tareas):
                tareas[opcion - 1]["completa"] = True
                print("[+] ¡Tarea marcada como completa!")
            else:
                print("[!] Número de tarea inválido.")
        except ValueError:
            print("[+] Ingrese un número válido.")

def opcion_tres():
    limpiar_pantalla()
    print("Aqui eliminaras una tarea.")

def opcion_cuatro():
    limpiar_pantalla()
    print("Tareas:")
    if not tareas:
        print("[!] No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"Tarea {i}:")
            print(f"Nombre: {tarea['nombre']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha límite: {tarea['fecha_limite']}")
            print(f"Hora límite: {tarea['hora_limite']}")
            print(f"Estado: {'completa' if tarea['completa'] else 'incompleta'}")
            print()

def opcion_cinco():
    limpiar_pantalla()
    print("[+] Estado de Tareas:")
    if not tareas:
        print("[!] No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            estado = "completa" if tarea["completa"] else "incompleta"
            print(f"Tarea {i}: {tarea['nombre']} - Estado: {estado}")

def opcion_seis():
    limpiar_pantalla()
    print("Aqui veras el reporte de todas tus tareas.")

def opcion_salir():
    print("\n\n[!] Saliendo...\n")

def opcion_invalida():
    limpiar_pantalla()
    print("[!] Número no válido. Por favor, ingresa un número del 1 al 7.")

opciones = {
    1: opcion_uno,
    2: opcion_dos,
    3: opcion_tres,
    4: opcion_cuatro,
    5: opcion_cinco,
    6: opcion_seis,
    7: opcion_salir,
}

while True:
    limpiar_pantalla()
    pyfiglet.print_figlet(text="task hero", colors='BLUE', font="isometric1")
    mostrar_menu()
    numero = int(input("Ingrese una opcion: "))
    limpiar_pantalla()
    if numero == 7:
        opciones[numero]()
        break
    else:
        opciones.get(numero, opcion_invalida)()
        input("Presiona Enter para continuar...")

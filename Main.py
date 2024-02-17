#!/usr/bin/python3
import os
import sys, signal, requests
import pyfiglet

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

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
    print("Aqui agregaras una nueva tarea.")

def opcion_dos():
    limpiar_pantalla()
    print("Marca las tareas que quieras como completadas.")

def opcion_tres():
    limpiar_pantalla()
    print("Aqui eliminaras una tarea.")

def opcion_cuatro():
    limpiar_pantalla()
    print("Aqui visualizaras tus tareas.")

def opcion_cinco():
    limpiar_pantalla()
    print("Aqui veras el estado de tus tareas.")

def opcion_seis():
    limpiar_pantalla()
    print("Aqui veras el reporte de todas tus tareas.")

def opcion_salir():
    print("\n\n[!] Saliendo...\n")

def opcion_invalida():
    limpiar_pantalla()
    print("Número no válido. Por favor, ingresa un número del 1 al 7.")

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
    text = pyfiglet.print_figlet(text="task hero", colors='BLUE', font="isometric1")
    mostrar_menu()
    numero = int(input("Ingrese una opcion: "))
    limpiar_pantalla()
    if numero == 7:
        opciones[numero]()
        break
    else:
        opciones.get(numero, opcion_invalida)()
        input("Presiona Enter para continuar...")
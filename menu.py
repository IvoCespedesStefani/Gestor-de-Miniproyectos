import tkinter as tk
from tkinter import Menu, simpledialog

proyectos = []

def crear_menu(root, cambiar_proyecto_callback, agregar_proyecto_callback):
    menubar = Menu(root)

    proyectos_menu = Menu(menubar, tearoff=0)

    def actualizar_menu_proyectos():
        proyectos_menu.delete(0, tk.END)  #Limpiar 
        for proyecto in proyectos:
            proyectos_menu.add_command(label=proyecto, command=lambda p=proyecto: cambiar_proyecto_callback(p))
        proyectos_menu.add_separator()
        proyectos_menu.add_command(label="Agregar nuevo proyecto", command=agregar_proyecto_callback)

    actualizar_menu_proyectos()
    menubar.add_cascade(label="Proyectos", menu=proyectos_menu)

    root.config(menu=menubar)

def agregar_proyecto(root):
    global proyectos
    nombre_proyecto = simpledialog.askstring("Nuevo Proyecto", "Nombre del proyecto:")
    if nombre_proyecto:
        proyectos.append(nombre_proyecto)
        crear_menu(root, cambiar_proyecto, lambda: agregar_proyecto(root)) 

def cambiar_proyecto(proyecto):
    print(f"Cambiando al {proyecto}")

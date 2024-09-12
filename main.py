import tkinter as tk
from menu import crear_menu, agregar_proyecto
from reloj import Cronometro
from lista import ListaTareasApp

proyecto_actual = None

def cambiar_proyecto_callback(proyecto):
    global proyecto_actual
    proyecto_actual = proyecto
    print(f"Proyecto actual: {proyecto}")
    etiqueta_proyecto.config(text=f"Proyecto actual: {proyecto}") 

cronometro = Cronometro()

def iniciar_cronometro():
    cronometro.iniciar()
    actualizar_tiempo()

def pausar_cronometro():
    cronometro.pausar()

def reiniciar_cronometro():
    cronometro.reiniciar()
    actualizar_tiempo()

def actualizar_tiempo():
    tiempo_mostrado.config(text=cronometro.mostrar_tiempo())
    if not cronometro.en_pausa:
        root.after(1000, actualizar_tiempo)

# Interfaz principal
root = tk.Tk()
root.title("Organizador de Proyectos")

etiqueta_proyecto = tk.Label(root, text="Proyecto actual: Ninguno", font=("Helvetica", 16))
etiqueta_proyecto.pack(pady=10)

crear_menu(root, cambiar_proyecto_callback, lambda: agregar_proyecto(root))

lista_tareas_app = ListaTareasApp(root)

frame_cronometro = tk.Frame(root)
frame_cronometro.pack(pady=10)

tiempo_mostrado = tk.Label(frame_cronometro, text="00:00:00.00", font=("Helvetica", 24))
tiempo_mostrado.pack()

botones_cronometro = tk.Frame(root)
botones_cronometro.pack(pady=10)

btn_iniciar = tk.Button(botones_cronometro, text="Iniciar", command=iniciar_cronometro)
btn_iniciar.pack(side=tk.LEFT, padx=5)

btn_pausar = tk.Button(botones_cronometro, text="Pausa", command=pausar_cronometro)
btn_pausar.pack(side=tk.LEFT, padx=5)

btn_reiniciar = tk.Button(botones_cronometro, text="Reiniciar", command=reiniciar_cronometro)
btn_reiniciar.pack(side=tk.LEFT, padx=5)

root.mainloop()

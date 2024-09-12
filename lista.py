import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.task_listbox = tk.Listbox(frame, height=10, width=50)
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.task_listbox.yview)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.pack(side=tk.LEFT)

        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Nueva tarea", command=self.agregar_tarea)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(button_frame, text="Editar tarea", command=self.editar_tarea)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(button_frame, text="Borrar tarea", command=self.eliminar_tarea)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def agregar_tarea(self):
        tarea = self.entry_task.get()
        if tarea:
            self.task_listbox.insert(tk.END, tarea)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

    def editar_tarea(self):
        try:
            tarea_index = self.task_listbox.curselection()[0]
            tarea_actual = self.task_listbox.get(tarea_index)
            nueva_tarea = self.entry_task.get()
            if nueva_tarea:
                self.task_listbox.delete(tarea_index)
                self.task_listbox.insert(tarea_index, nueva_tarea)
                self.entry_task.delete(0, tk.END)
            else:
                messagebox.showwarning("Advertencia", "No puedes dejar la tarea vacía.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para editar.")

    def eliminar_tarea(self):
        try:
            tarea_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(tarea_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

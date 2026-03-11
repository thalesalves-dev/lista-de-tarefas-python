import tkinter as tk
from task import Task

tasks = []

def add_task():
    title = entry_title.get()
    description = entry_desc.get()
    if title:
        task = Task(title, description)
        tasks.append(task)
        update_listbox()
        entry_title.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, str(task))

root = tk.Tk()
root.title("Lista de Tarefas")

tk.Label(root, text="Título:").pack()
entry_title = tk.Entry(root)
entry_title.pack()

tk.Label(root, text="Descrição:").pack()
entry_desc = tk.Entry(root)
entry_desc.pack()

tk.Button(root, text="Adicionar Tarefa", command=add_task).pack()
listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.pack()

root.mainloop()

import tkinter as tk
from tarefa import Tarefa

tarefas = []

def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                titulo, descricao = linha.strip().split("|")
                tarefas.append(Tarefa(titulo, descricao))
    except FileNotFoundError:
        pass

def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa.titulo}|{tarefa.descricao}\n")

def adicionar_tarefa():
    titulo = entrada_titulo.get()
    descricao = entrada_descricao.get()

    if titulo:
        tarefa = Tarefa(titulo, descricao)
        tarefas.append(tarefa)
        atualizar_lista()
        salvar_tarefas()

        entrada_titulo.delete(0, tk.END)
        entrada_descricao.delete(0, tk.END)

def remover_tarefa():
    selecionado = lista_tarefas.curselection()
    if selecionado:
        tarefas.pop(selecionado[0])
        atualizar_lista()
        salvar_tarefas()

def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for tarefa in tarefas:
        lista_tarefas.insert(tk.END, str(tarefa))

carregar_tarefas()

janela = tk.Tk()
janela.title("Lista de Tarefas")

tk.Label(janela, text="Título").pack()
entrada_titulo = tk.Entry(janela)
entrada_titulo.pack()

tk.Label(janela, text="Descrição").pack()
entrada_descricao = tk.Entry(janela)
entrada_descricao.pack()

tk.Button(janela, text="Adicionar", command=adicionar_tarefa).pack()
tk.Button(janela, text="Remover", command=remover_tarefa).pack()

lista_tarefas = tk.Listbox(janela, width=50)
lista_tarefas.pack()

atualizar_lista()

janela.mainloop()

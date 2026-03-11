class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def __str__(self):
        return f"{self.titulo} - {self.descricao}"

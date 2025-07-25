class Condition:
    def __init__(self, nome: str, efeitos_mecanicos: list[str], duracao_tipica: str):
        self.nome = nome
        self.efeitos_mecanicos = efeitos_mecanicos
        self.duracao_tipica = duracao_tipica 
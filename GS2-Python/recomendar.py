class Recomendador:
    def __init__(self, carreiras_disponiveis):
        self.carreiras = carreiras_disponiveis

    def recomendar(self, perfil):
        resultados = []
        for carreira in self.carreiras:
            pontuacao = carreira.compatibilidade(perfil)
            if pontuacao > 0:
                resultados.append((carreira.nome, pontuacao))
        resultados.sort(key=lambda x: x[1], reverse=True)
        return [nome for nome, _ in resultados]

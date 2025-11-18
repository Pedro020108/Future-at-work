class Carreira:
    def __init__(self,nome,competencias_revelantes):
        self.nome = nome
        self.competencias_revelantes = competencias_revelantes

    def compatibilidade(self, perfil):
        match = 0
        for comp in self.competencias_revelantes:
            if comp in perfil.competencias:
                match+=1

        return match
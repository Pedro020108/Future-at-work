class Perfil:
    def __init__(self, nome, idade, area_inte):
        self.nome = nome
        self.idade = idade
        self.area_inte = area_inte
        # lista para armazenamento
        self.competencias = []
        self.experiencias = []
        self.certificados = []

    def adicionar_competencia(self, competencia):
        if competencia not in self.competencias:
            self.competencias.append(competencia)

    def adicionar_experiencia(self, experiencia):
        self.experiencias.append(experiencia)

    def adicionar_certificado(self, certificado):
        self.certificados.append(certificado)

    def resumo(self):
        return {
            "Nome": self.nome,
            "Idade": self.idade,
            "Área de Interesse": self.area_inte,
            "Competências": self.competencias,
            "Experiências": self.experiencias,
            "Certificados": self.certificados
        }

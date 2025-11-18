from perfil import Perfil
from carreira import Carreira
from recomendar import Recomendador

def main():
    perfil1 = Perfil("Michael", 45, "Desenvolvedor Back-End")
    perfil1.adicionar_competencia ("Python")
    perfil1.adicionar_competencia ("C++")
    perfil1.adicionar_competencia("Java")
    perfil1.adicionar_experiencia("Projeto automação residencial")
    perfil1.adicionar_experiencia("Projeto de controle de estoque")
    perfil1.adicionar_certificado("Inglês")
    perfil1.adicionar_certificado("Python básico")

    carreiras = [
        Carreira("Desenvolvedor de Software", ["Python", "Lógica", "Colaboração"]),
        Carreira("Designer de Inovação", ["Criatividade", "Adaptabilidade", "Colaboração"]),
        Carreira("Analista de Dados", ["Python", "Lógica", "Adaptabilidade"])
    ]

    recomendador = Recomendador(carreiras)

    perfis = [perfil1]

    for perfil in perfis:
        print(f"--- Perfil: {perfil.nome} ---")
        resumo = perfil.resumo()
        for chave, valor in resumo.items():
            print(f"{chave}: {valor}")
        print("\nRecomendações de carreira:")
        print(recomendador.recomendar(perfil))
        print("\n" + "-" * 40 + "\n")


if __name__ == "__main__":
    main()
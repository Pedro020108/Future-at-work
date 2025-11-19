# GS2 - Future at Work

## Descrição do projeto
Este projeto foi desenvolvido para o desafio Global Solution 2025.2, no curso de Ciência da Computação.  
O objetivo é criar uma ferramenta simples que analisa perfis profissionais e gera recomendações de carreiras, com base em competências, experiências e certificados do usuário.

## Funcionalidades
- Cadastro de perfis com informações como nome, idade, área de interesse, competências, experiências e certificados.
- Cadastro de carreiras com competências relevantes.
- Avaliação da compatibilidade entre perfis e carreiras.
- Geração de recomendações ordenadas de acordo com a compatibilidade.

## Estrutura do projeto
- `perfil.py` : define a classe `Perfil` para armazenar e organizar dados do usuário.  
- `carreira.py` : define a classe `Carreira` com competências relevantes de cada carreira.  
- `recomendar.py` : define a classe `Recomendador`, responsável por avaliar perfis e recomendar carreiras.  
- `main.py` : arquivo principal que cria os perfis e carreiras, executa a análise e imprime os resultados.

## Como executar
1. Clone o repositório:  
   `git clone https://github.com/Pedro020108/Future-at-work/tree/main/GS2-Python`   
2. Entre na pasta do projeto:  
    `GS2-Python`  
3. Execute o script principal:  
   `python main.py`  
4. Confira no terminal o resumo do perfil e as recomendações de carreira.

## Sobre o código
O sistema é feito em Python usando Programação Orientada a Objetos. Ele organiza os dados em classes e usa listas e dicionários para armazenar informações. A análise é feita verificando quantas competências do perfil coincidem com as competências de cada carreira.

## Link do Vídeo do Youtube

https://youtu.be/zbQqWZ_9ncs 

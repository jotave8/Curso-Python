Repositório destinado a expor as atividades feitas durante o meu aprendizado sobre Python no Curso do Gustavo Guanabara.


📌Tipos Primitivos e Saída de Dados em Python

-Tipos Primitivos
    Em Python, os principais tipos primitivos são:
        int → Números inteiros (ex: 10, -5)
        float → Números decimais (ex: 3.14, -0.5)
        str → Texto (ex: "Python", '123')
        bool → Booleano (True ou False)

    O input() sempre retorna uma string, então conversões são necessárias:
        num = int(input("Digite um número: "))  # Converte para inteiro

-Saída de Dados
    Para exibir valores, usamos print():
        nome = "João"
        idade = 25
        print(f"Meu nome é {nome} e tenho {idade} anos.")

    Outras formas:
        print("Meu nome é {} e tenho {} anos.".format(nome, idade))
        print("Meu nome é", nome, "e tenho", idade, "anos.")
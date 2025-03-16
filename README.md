# Python Learning Repository

Repositório destinado a expor as atividades feitas durante o meu aprendizado sobre Python no Curso do Gustavo Guanabara.

## 📌 Tipos Primitivos e Saída de Dados em Python

### Tipos Primitivos
    Em Python, os principais tipos primitivos são:
        int → Números inteiros (ex: 10, -5)
        float → Números decimais (ex: 3.14, -0.5)
        str → String (ex: "Python", '123')
        bool → Booleano (True ou False)

    O input() sempre retorna uma string, então conversões são necessárias:
        num = int(input("Digite um número: "))  # Converte para inteiro

### Saída de Dados
    Para exibir valores, usamos print():
        nome = "João"
        idade = 25
        print(f"Meu nome é {nome} e tenho {idade} anos.")

    Outras formas:
        print("Meu nome é {} e tenho {} anos.".format(nome, idade))
        print("Meu nome é", nome, "e tenho", idade, "anos.")

## 📌 Operadores Aritméticos em Python

    Os operadores aritméticos realizam cálculos matemáticos com números.

    Operador    Descrição          Exemplo    Resultado
    +           Adição             5 + 3      8
    -           Subtração          10 - 4     6
    *           Multiplicação      6 * 2      12
    /           Divisão real       9 / 2      4.5
    //          Divisão inteira    9 // 2     4
    %           Módulo (resto)     10 % 3     1
    **          Exponenciação      2 ** 3     8

### Precedência dos Operadores Aritméticos
    A ordem de precedência dos operadores aritméticos em Python é a seguinte:
        1. Parênteses: ()
            - Operações dentro de parênteses têm a maior precedência.
        2. Exponenciação: **
            - Calculado da direita para a esquerda.
        3. Multiplicação, Divisão, Divisão Inteira e Módulo: *, /, //, %
            - Calculados da esquerda para a direita.
        4. Adição e Subtração: +, -
            - Calculados da esquerda para a direita.

    Exemplo:
        resultado = 10 + 3 * 2 ** 2  # Resultado: 22
        resultado = (10 + 3) * 2 ** 2  # Resultado: 52

## 📌 Módulos em Python

### O que são módulos
    - Módulos são arquivos Python com funções, classes e variáveis que podem ser reutilizados em outros programas.
    - Permitem organizar o código e evitar repetição.

### Como importar módulos
    Usando `import` para carregar o módulo inteiro:
        import math
        raiz = math.sqrt(25)

    Usando `from/import` para trazer partes específicas:
        from math import sqrt
        raiz = sqrt(25)

### Módulos built-in
    São módulos que já vêm instalados com Python. Exemplos:
        math → Funções matemáticas (sqrt, pow, sin).
        random → Geração de números aleatórios.
        datetime → Manipulação de datas e horas.
        os → Interação com o sistema operacional.

### Módulos externos (PyPI)
    Módulos adicionais podem ser instalados via **PyPI** usando o `pip`:
        Instalação (no terminal):
            pip install nome_do_modulo

        Exemplos populares:
            numpy → Cálculos numéricos.
            pandas → Análise de dados.

### Exemplo prático
    Importando e usando o módulo `random`:
        import random
        numero = random.randint(1, 10)

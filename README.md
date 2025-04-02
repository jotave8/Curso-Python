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

## 📌 Manipulação de Strings em Python

### Fatiamento (Slicing)

    texto = "Aprendendo Python"

    print(texto[0])         # "A" (primeiro caractere)
    print(texto[3:9])       # "endend" (do índice 3 ao 8)
    print(texto[::2])       # "ApedoPto" (pula de 2 em 2)
    print(texto[::-1])      # "nohtyP odnerpA" (inverte a string)

### Análise

    texto = "Curso de Python"

    print(len(texto))           # 14 (comprimento da string)
    print(texto.count("o"))     # 3 (quantas vezes "o" aparece)
    print(texto.find("de"))     # 5 (índice onde começa "de")
    print("Python in texto")    # True (verifica se existe na string)

### Transformações

    texto = "  python é fácil  "

    print(texto.upper())                        # "  PYTHON É FÁCIL  " (converte para maiúsculas)
    print(texto.lower())                        # "  python é fácil  " (converte para minúsculas)
    print(texto.capitalize())                   # "  python é fácil  " → "  Python é fácil  " (primeira letra maiúscula)
    print("python".title())                     # "  Python É Fácil  " (primeira letra de cada palavra maiúscula)
    print(texto.strip())                        # "python é fácil" (remove espaços das bordas)
    print(texto.replace("fácil", "poderoso"))   # "  python é poderoso  " (troca uma palavra por outra)

### Junção

    lista = ["Python", "é", "incrível"]
    print("-".join(lista))  # "Python-é-incrível"

### Principais Métodos

| Método          | Ação                                | Exemplo                          |
|-----------------|-------------------------------------|----------------------------------|
| `len()`         | Retorna o comprimento da string     | `len("ola")` → `3`               |
| `count("x")`    | Conta ocorrências de "x"            | `"ola".count("o")` → `1`         |
| `find("x")`     | Retorna o índice de "x"             | `"ola".find("l")` → `1`          |
| `replace(a, b)` | Substitui "a" por "b"               | `"hi".replace("h", "o")` → `"oi"`|
| `strip()`       | Remove espaços das bordas           | `" texto ".strip()` → `"texto"`  |
| `join()`        | Junta elementos de uma lista        | `"-".join(["a", "b"])` → `"a-b"` |

## 📌 Condições em Python (Parte 1)

    Estruturas condicionais permitem que seu programa tome decisões!

### Estrutura Básica

#### Condicional Simples (if)
    Executa um bloco de código apenas se a condição for verdadeira:

        idade = 18
        if idade >= 18:
            print("Você pode votar!")  # Só roda se idade >= 18

#### Condicional Composta (if/else)
    Define ações para dois cenários (verdadeiro ou falso):

        temperatura = 25
        if temperatura > 30:
            print("Dia quente! 🌞")
        else:
            print("Clima ameno! 😊")  # Roda se temperatura <= 30

### Operadores de Comparação

| Operador	| Significado	  | Exemplo	| Resultado (True) |
|-----------|-----------------|---------|------------------|
|  ==	    | Igual	          | 5 == 5	| ✅               |
|  !=	    | Diferente	      | 3 != 2	| ✅               |
|  >	    | Maior que	      | 10 > 5	| ✅               |
|  <	    | Menor que	      | 5 < 10	| ✅               |
|  >=	    | Maior ou igual  | 7 >= 7	| ✅               |
|  <=	    | Menor ou igual  | 4 <= 5	| ✅               |

### Operadores Lógicos

| Operador	| Significado	        | Exemplo	          | Resultado (True) |
|-----------|-----------------------|---------------------|------------------|
| and	    | E (ambas condições)	|(5 > 3) and (2 == 2) |	✅               |
| or	    | Ou (pelo menos uma)	|(5 < 3) or (2 == 2)  |	✅               |
| not	    | Não (inverte o valor)	|not (5 < 3)	      | ✅               | 

### Exemplos Práticos
    1. Verificar se um número é par ou ímpar
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("É par!")
        else:
            print("É ímpar!")

    2. Sistema de login básico
        senha_correta = "python123"
        senha = input("Digite sua senha: ")

        if senha == senha_correta:
            print("Acesso permitido!")
        else:
            print("Senha incorreta!")

    3. Verificar múltiplas condições
        idade = 20
        tem_ingresso = True

        if idade >= 18 and tem_ingresso:
            print("Pode entrar no evento!")
        else:
            print("Acesso negado!")

### Aninhando Condições
    Você pode colocar um if dentro de outro:

        numero = 10
        if numero > 0:
            print("Positivo")
            if numero % 2 == 0:
                print("e par!")
        else:
            print("Negativo ou zero")
'''Um professor quer sortear um dos quatro alunos para apagar o quadra. Faça um programa que ajude ele lendo o nome
deles e escrevendo o nome do escolhido'''

from random import choice

aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
alunos = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(alunos)
print('O aluno escolhido foi {}'.format(escolhido))
'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada'''

from random import shuffle

aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
alunos = [aluno1,aluno2,aluno3,aluno4]
shuffle(alunos)
print('\nOrdem de apresentação')
print('1°: {}'.format(alunos[0]))
print('2°: {}'.format(alunos[1]))
print('3°: {}'.format(alunos[2]))
print('4°: {}'.format(alunos[3]))
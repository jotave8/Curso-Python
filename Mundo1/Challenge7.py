#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
media = (nota1 + nota2)/2
print('A sua média é {:.1f}'.format(media))
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

grade1 = float(input('Enter your first grade: '))
grade2 = float(input('Enter your second grade: '))
average = (grade1 + grade2)/2
print('Your average is {:.1f}'.format(average))
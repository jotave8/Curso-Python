#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor

num = int(input('Digite um número inteiro: '))
ant = num - 1
sus = num + 1
print('O antecessor de {} é {}\nO sucessor de {} é {}'.format(num, ant, num, sus))
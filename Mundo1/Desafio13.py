#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Informe o seu salário: '))
aumento = salario*1.15
print('Considerando um aumento de 15% no seu salário, vocé vai passar a receber R${:.2f}'.format(aumento))
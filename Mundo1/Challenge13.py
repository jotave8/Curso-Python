#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Informe salário do funcionário: '))
aumento = salario*1.15
print('Considerando um aumento de 15% no salário, o funcionário vai passar a receber R${:.2f}'.format(aumento))
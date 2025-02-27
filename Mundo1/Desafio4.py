#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

var = input('Digite algo: ')
print('O tipo primitivo dessa variável é {}'.format(type(var)))
print('É númerico? {}'.format(var.isnumeric()))
print('É letra? {}'.format(var.isalpha()))
print('É alfanúmerico? {}'.format(var.isalnum()))
print('Está em maiusculo? {}'.format(var.isupper()))
print('Está em minusculo? {}'.format(var.islower()))
print('Está capitalizada? {}'.format(var.istitle()))
print('Só tem "espaço"? {}'.format(var.isspace()))
print('É printável? {}'.format(var.isprintable()))
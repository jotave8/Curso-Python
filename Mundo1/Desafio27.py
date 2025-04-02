''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente'''

full_name = str(input('Enter your full name: ')).strip()
name = full_name.split()
print('Your first name is {} and your last name is {}'.format(name[0],nome[len(name-1)])

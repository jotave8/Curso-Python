''' Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome '''

name = str(input('Provide your name: '))
name = name.upper()
print('Your name has "SILVA": {}'.format("SILVA" in name))
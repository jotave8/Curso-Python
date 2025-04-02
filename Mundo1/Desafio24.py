''' Crie um programa que leia o nome de uma cidade e diga se ela começa ou não como nome 'SANTO' '''

city = str(input('Informe o nome da cidade: '))
city = city.upper()
space = city.find(" ")
name = city[0:space]
print('O nome da cidade começa com "SANTO": {}'.format("SANTO" in name))
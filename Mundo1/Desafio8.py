#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metro = int(input('Informe o valor em metros: '))
centi = metro*100
mili = metro*1000
print('{}m equivale a {}cm\n{}m equivale a {}mm'.format(metro, centi, metro, mili))
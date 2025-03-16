'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e 
mostre o comprimento da hipotenusa'''
from math import sqrt


print('Considerando um triângulo retângulo')
cateopos = int(input('Informe o comprimento do cateto oposto: '))
cateadja = int(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = sqrt((pow(cateopos,2)+pow(cateadja,2)))
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(hipotenusa))
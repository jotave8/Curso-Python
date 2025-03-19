'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e 
mostre o comprimento da hipotenusa'''
from math import hypot

print('Considerando um triângulo retângulo')
co = int(input('Informe o comprimento do cateto oposto: '))
ca = int(input('Informe o comprimento do cateto adjacente: '))
hip = hypot(co,ca)
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(hip))
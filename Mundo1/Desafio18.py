#Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente desse ângulo
from math import sin,cos,tan,radians

valor = int(input('Informe o valor do angulo: '))
angulo = radians(valor)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print('Informações sobre o ângulo de {}°:\nSeno: {:.1f}\nCosseno: {:.1f}\nTangente:{:.1f}'.format(angulo,seno,cosseno,tangente))
''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados em unidade, dezena
centena e milhar'''

num = int(input('Informe um numero de 0 a 9999: '))
uni = num%10
dez = (num//10)%10
cen = (num//100)%10
mil = (num//1000)%10

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
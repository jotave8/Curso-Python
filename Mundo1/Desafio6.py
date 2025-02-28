#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número: '))
double = num*2
triple = num*3
square = float(num**(1/2))
print('O dobro de {} é {}'.format(num, double))
print('O triplo de {} é {}'.format(num, triple))
print('A raiz quadrada de {} é {:.2f}'.format(num, square))
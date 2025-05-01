#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Enter a number: '))
double = num*2
triple = num*3
square = float(num**(1/2))

print('Double the amount of {} is {}'.format(num, double))
print('Triple the amount of {} is {}'.format(num, triple))
print('The square root of {} is {:.2f}'.format(num, square))
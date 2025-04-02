''' Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome '''

nome = str(input('Informe seu nome completo: '))
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letra (sem contar os espaços)'.format(len(nome.replace(" ",""))))
print('Seu primeiro nome tem {} letras'.format(nome.find(" ")))
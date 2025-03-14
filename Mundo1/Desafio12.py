#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor = float(input('Informe o valor do produto: R$'))
desconto = valor*0.95
print('O produto custa R${:.2f} e aplicando o desconto de 5% fica por R${:.2f}'.format(valor, desconto))

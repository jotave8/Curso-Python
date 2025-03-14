#Crie um programa que leia quanto uma pessoa tem na carteira e mostra quantos dólares ela pode comprar

carteira=float(input('Informe quanto reais você tem na carteira: '))
dolar = carteira/5.5
print('Você pode comprar ${:.2f}'.format(dolar))
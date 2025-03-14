#Crie um programa que leia quanto uma pessoa tem na carteira e mostra quantos dólares ela pode comprar

carteira=float(input('Informe quanto reais você tem na carteira: R$'))
dolar = carteira/5.5
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(carteira,dolar))
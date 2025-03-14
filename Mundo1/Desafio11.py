'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²'''

largura = float(input('Informe a altura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura*altura
tinta = area/2
print('A parede tem {:.2f}m², será necessário {:.1f}L de tinta'.format(area,tinta))
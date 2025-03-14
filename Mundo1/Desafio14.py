#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

celsius = float(input('Informe a temperatura em Celsius: '))
fahrenheit = celsius*9/5+32
print('{:.1f}°C equivale a {:.1f}°F'.format(celsius, fahrenheit))
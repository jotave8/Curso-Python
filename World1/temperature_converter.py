#Write a program that converts a temperature entered in °C and converts it to °F

celsius = float(input('Enter the temperature in Celsius: '))
fahrenheit = celsius*9/5+32
print('{:.1f}°C is equivalent to {:.1f}°F'.format(celsius, fahrenheit))
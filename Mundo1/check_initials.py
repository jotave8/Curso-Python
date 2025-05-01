''' Create a program that reads the name of a city and says whether or not it starts with a name 'SANTO' '''

city = str(input('Enter the name of the city: '))
city = city.upper()
space = city.find(" ")
name = city[0:space]
print('The name of the city begins with "SANTO": {}'.format("SANTO" in name))
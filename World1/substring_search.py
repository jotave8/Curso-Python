''' Create a program that reads a person's name and says if they have 'SILVA' in their name '''

name = str(input('Provide your name: '))
name = name.upper()
print('Your name has "SILVA": {}'.format("SILVA" in name))
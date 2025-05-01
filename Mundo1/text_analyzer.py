''' Create a program that reads a person's full name and displays:
- The name in all capital letters
- The name in all lowercase letters
- How many letters in total (without considering spaces)
- How many letters does the first name have '''

name = str(input('Enter your full name: '))
print('Your name in uppercase is {}'.format(name.upper()))
print('Your name in lowercase is {}'.format(name.lower()))
print('Your name has {} letters (without counting spaces)'.format(len(name.replace(" ",""))))
print('Your first name has {} letters'.format(name.find(" ")))
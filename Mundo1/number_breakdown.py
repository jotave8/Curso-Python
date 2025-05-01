#Create a program that reads any Real number from the keyboard and displays its integer portion on the screen
#Ex.: Enter a number: 6,127 The number 6,127 has an integer portion of 6

from math import floor

num = float(input('Enter a number: '))
integer = floor(num)
print('The integer portion of the number {} is {}'.format(num, integer))
'''Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to figure out 
which number the computer chose. The program should write on the screen whether the user won or lost.'''

from random import randint
from time import sleep

computer = randint(0,5)
print('The computer is choosing a number...')
sleep(1)
print('Chosen number!!')
user = int(input('Try to guess wich number between 0 and 5 was chosen: '))
if user == computer:
    print('Congratulations, you got it right!!!')
else:
    print('Sorry, you made a mistake. The numer chosen by the computer was {}.'.format(computer))
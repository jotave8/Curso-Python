'''Write a program that reads the length of the opposite and adjacent legs of a right triangle. Calculate and 
display the length of the hypotenuse'''
from math import hypot

print('Considering a right triangle')
os = int(input('Enter the length of the opposite side: '))
ads = int(input('Enter the length of the adjacent side: '))
hip = hypot(os,ads)
print('The hypotenuse of this right triangle is {:.2f}'.format(hip))
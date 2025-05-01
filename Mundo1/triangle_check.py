# Develop a program that reads the lenght of three lines and tells the user whether or not they can form a triangle

line1 = int(input('Enter the size of the first line: '))
line2 = int(input('Enter the size of the second line: '))
line3 = int(input('Enter the size of the third line: '))

if (line1 + line2 > line3) and (line1 + line3 > line2) and (line3 + line2 > line1):
    print('These lines can form a triangle.')
else:
    print('These lines cannot form a triangle.')
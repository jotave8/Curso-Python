''' Redo the triangle check program, adding the feature to what type of triangle will be formed:
- Equilateral: all sides equal
- Isosceles: two sides equal
- Scalene: all sides different '''

line1 = int(input('Enter the size of the first line: '))
line2 = int(input('Enter the size of the second line: '))
line3 = int(input('Enter the size of the third line: '))

if (line1 + line2 > line3) and (line1 + line3 > line2) and (line3 + line2 > line1):
    if line1 == line2 == line3:
        print('\nThese lines form a equilateral triangle.')
    elif line1 != line2 != line3:
        print('\nThese lines form a Scalene triangle.')
    else:
        print('\nThese lines form Isosceles a triangle.')
else:
    print('\nThese lines cannot form a triangle.')
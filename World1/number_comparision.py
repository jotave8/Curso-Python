''' Whrite a program that reads twos integers and compares them, displaying a message on the screen: 
- The first value is greater
- The second value is greater
- There is no greater value, both are equal '''

value1 = int(input('Enter the first number: '))
value2 = int(input('Enter the second number: '))

if value1 > value2:
    print('\nThe first value is greater.')
elif value2 > value1:
    print('\nThe second value is greater.')
else:
    print('\nThere is no greater value, both are equal.')
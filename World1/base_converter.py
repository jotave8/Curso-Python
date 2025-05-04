''' Write a program that reads any integer and asks the user to choose the conversion base:
- 1 for binary
- 2 for octal
- 3 for hexadecimal '''

number = int(input('Enter a integer number: '))

base = int(input('\n 1 - Binary\n 2 - Octal\n 3 - Hexadecimal\n Choose which base you want to convert the entered number to: '))
if base == 1:
    print(f'The number {number} converted to Binary is {bin(number)[2:]}')
elif base == 2: 
    print(f'The number {number} converted to Octal is {oct(number)[2:]}')
elif base == 3:
    print(f'The number {number} converted to Hexadecimal is {hex(number)[2:]}')
else: 
    print('Invalid conversion.')
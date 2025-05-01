''' Write a program that reads a number from 0 to 9999 and displays each digit on the screen, 
separated into units, tens, hundreds and thousands'''

num = int(input('Enter a number from 0 to 9999: '))
unit = num%10
tens = (num//10)%10
hundred = (num//100)%10
thousand = (num//1000)%10

print('Unit: {}'.format(unit))
print('Tens: {}'.format(tens))
print('Hundred: {}'.format(hundred))
print('Thousand: {}'.format(thousand))
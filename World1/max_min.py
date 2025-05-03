# Make a program that reads three numbers ands shows which is the biggest and which is the smallest

num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
num3 = int(input('Enter the third number:'))

biggest = max(num1,num2,num3)
smallest = min(num1,num2,num3)

print(f'The biggest number is {biggest} and the smallest number is {smallest}')

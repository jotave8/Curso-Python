''' Write a program that asks an employee for his/her salary and calculates the amount of his/her salary increase.
For salaries greater than R$1250, calculate a 10% increase.
For salaries lower than or equal to R$1250, the increase is 15%.'''

salary = float(input('Enter employee salary: '))

if salary > 1250: 
    salary *= 1.1
else:
    salary *= 1.15

print(f'His/her new salary is R${salary}')
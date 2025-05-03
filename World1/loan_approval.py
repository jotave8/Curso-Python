'''Write a program to approve a bank loan to buy a house. The program will ask for the value of the house, 
the buyer's salary and how many years he will pay it back. Calculate the monthly payment amount, 
knowing that it cannot exceed 30% of the salary or else the loan will be denied.'''

house = float(input('Enter the value of the house: '))
salary = float(input("Enter the buyer's salary: "))
years = int(input('Inform in how many years the buyer will pay: '))

payment = house / (years * 12)

print(f'\nTo pay for a house worth R${house:.2f} in {years} years, the installment will be R${payment:.2f}')

if payment > (salary*0.3):
    print("Loan denied because the installment amount exceeds 30% of the buyer's salary")
else:
    print(f'Loan approved!!!')
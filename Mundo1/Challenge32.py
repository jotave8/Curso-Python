# Make a program that reads a any year and shows if it is a leap year
from datetime import datetime

year = int(input('Choise a year (If you want the current year, enter 0): '))
if year == 0: 
    year = datetime.now().year
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} isn't a leap year.")
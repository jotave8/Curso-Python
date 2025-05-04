''' The National Swimming Confederation needs a program that reads an athlete's year of birth and shows their category,
according to age: 
- Up to 9 years old: MIRIM             - Up to 25 years old: SENIOR
- Up to 14 years old: INFANTIL         - Above: MASTER
- Up to 19 years old: JUNIOR '''

from datetime import datetime

year = int(input("Enter the athlete's year of birth: "))
age = datetime.now().year - year

if age < 0:
    print('Invalid age.')
elif age <= 9:
    print("The athlete's classification is Mirim")
elif age <= 14:
    print("The athlete's classification is Infantil")
elif age <= 19:
    print("The athlete's classification is Junior")
elif age <= 25:
    print("The athlete's classification is Senior")
else:
    print("The athlete's classification is Master")
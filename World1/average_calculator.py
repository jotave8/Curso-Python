''' Create a program that reads two grades from a student and calculates their average, displaying a message at the end
according to average achieved:
Average bellow 5.0: FAIL
Average between 5.0 and 6.9: RECOVERY
Average 7.0 or higher: PASSED '''

grade1 = float(input('Enter the your first grade: '))
grade2 = float(input('Enter the your second grade: '))
average = (grade1 + grade2)/2

if average < 5.0:
    print(f'\nAverage bellow 5.0: FAIL \nYour average: {average:.1f}')
elif average >= 5.0 and average <= 6.9:
    print(f'\nAverage between 5.0 and 6.9: RECOVERY \nYour average: {average:.1f}')
else: 
    print(f'\nAverage 7.0 or higher: PASSED \nYour average: {average:.1f}')
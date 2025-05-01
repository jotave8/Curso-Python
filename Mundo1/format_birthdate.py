#Create a Python script that reads the day, month, and year of a person's birth and displays a message with the formatted data

day = input("Enter the day of your birth: ")
month = input("Enter the month of your birth: ")
year = input("Enter the year of your birth: ")

print('Your birth date is {}/{}/{}'.format(day,month,year))
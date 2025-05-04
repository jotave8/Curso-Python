''' Make a program that read the year of birth of a young person and informs, according to their age, wether they are still
going to enlist in the military, whether it is time to enlist or whether it is past the enlistment period. Your program
should also show the time remaining or the time that has passed.'''

from datetime import datetime

year = int(input('Enter your year of birth: '))
enlistment = datetime.now().year - year

if enlistment < 18:
    print(f"It's not yet time to enlist, there are {18 - enlistment} year(s) left.")
elif enlistment == 18:
    print(f"You are in the period to enlist, do it this year. Go to a Military Service Board.")
else:
    print(F'You missed the deadline to enlist, you are {enlistment - 18} years late. Go to a Military Service Board as soon as possible.')
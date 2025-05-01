'''A teacher wants to draw lots for the order in which students will present their work. Write a program
that reads the names of the four students and shows the order drawn'''

from random import shuffle

student1 = str(input('Enter the name of the first student: '))
student2 = str(input('Enter the name of the second student: '))
student3 = str(input('Enter the name of the third student: '))
student4 = str(input('Enter the name of the fourth student: '))
students = [student1,student2,student3,student4]
shuffle(students)
print('\nOrder of presentation')
print('1st: {}'.format(students[0]))
print('2nd: {}'.format(students[1]))
print('3rd: {}'.format(students[2]))
print('4th: {}'.format(students[3]))
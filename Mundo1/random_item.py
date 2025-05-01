'''A teacher wants to randomly select one of the four students to erase the court. 
Write a program that helps him by reading their names and writing the name of the chosen one'''

from random choice import

student1 = str(input('Enter the name of the first student: '))
student2 = str(input('Enter the name of the second student: '))
student3 = str(input('Enter the name of the third student: '))
student4 = str(input('Enter the name of the fourth student: '))
students = [student1,student2,student3,student4]
chosen = choice(students)
print('The chosen student was {}'.format(chosen))
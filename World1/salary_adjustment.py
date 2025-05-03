
#Create an algorithm that reads an employee's salary and shows their new salary with a 15% increase

salary = float(input("Enter employee's salary: "))
increase = salary*1.15
print('Considering a 15% increase in salary, the employee will now receive R${:.2f}'.format(increase))
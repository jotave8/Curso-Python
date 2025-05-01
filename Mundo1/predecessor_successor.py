#Make a program that reads an integer and displays its successor and predecessor on the screen

num = int(input('Enter an integer: '))
pre = num - 1
suc = num + 1
print('The predecessor of {} is {}\nThe successor of {} is {}'.format(num, pre, num, suc))
#Make a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen

var = input('Type something: ')
print('The primitive type of this variable is {}'.format(type(var)))
print('Is it numeric? {}'.format(var.isnumeric()))
print('Is it letter? {}'.format(var.isalpha()))
print('Is it alphanumeric? {}'.format(var.isalnum()))
print('Is it uppercase? {}'.format(var.isupper()))
print('Is it lowercase? {}'.format(var.islower()))
print('Is it capitalized? {}'.format(var.istitle()))
print('Is it only "space"? {}'.format(var.isspace()))
print('Is it printable? {}'.format(var.isprintable()))
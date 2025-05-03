#Write a program that reads a value in meters and displays it converted to centimeters and millimeters

meter = int(input('Enter the value in meters: '))
centi = meter*100
milli = meter*1000
print('{}m is equivalent to {}cm\n{}m is equivalent to {}mm'.format(meter, centi, meter, milli))
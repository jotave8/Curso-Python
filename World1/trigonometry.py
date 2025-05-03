
#Make a program that reads any angle and shows the value of the sine, cosine and tangent of that angle
from math import sin,cos,tan,radians

value = int(input('Enter the value of the angle: '))
angle = radians(value)
sine = sin(angle)
cosine = cos(angle)
tangent = tan(angle)
print('Information about the angle of {}°:\nSine: {:.1f}\nCosine: {:.1f}\nTangent:{:.1f}'.format(angle,sine,cosine,tangent))
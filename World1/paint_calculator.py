'''Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint 
needed to paint it, knowing that each liter of paint paints an area of ​​2m²'''

width = float(input('Enter the height of the wall: '))
height = float('Enter the height of the wall: '))
area = width*height
paint = area/2
print('The wall is {:.2f}m², you will need {:.1f}L of paint'.format(area,paint))
'''Write a program that reads the speed of a car. If it exceeds 80km/h, display a message saying that it has been fined.
The fine will cost R$7,00 for each km over the limit.'''

speed = int(input('Enter car speed: '))
if speed > 80 :
    fine = (speed - 80)*7
    print("You exceeded the speed limit and were fined. The fine is R${:.2f}".format(fine))
else:
    print("Speed within the road limit!")
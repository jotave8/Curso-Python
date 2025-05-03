'''Write a program that asks for the number of km traveled by a rented car and the number of days for which it was rented. 
Calculate the price to be paid knowing that the car costs R$60 per day and R$0.15 per km driven'''

days = int(input('For how many days was the car rented? '))
km = float(input('How many km were driven in this period? '))
value = (days*60+km*0.15)
print('The car was rented for {} day(s) and traveled {:.1f}km. The amount to be paid is R${:.2f}'.format(days,km,value))
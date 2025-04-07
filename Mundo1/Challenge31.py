'''Develop a program that asks for the distance of a trip in Km. Calcule the price of the ticket charging R$0.5 per
Km for trips up to 200Km and R$0.45 for longer trips'''

trip = int(input('Enter the distance of a trip in Km: '))
if trip <= 200:
    ticket = trip * 0.5
else:
    ticket = trip * 0.45
    
print('The price of the ticket is R${:.2f}'.format(ticket))
#Create an algorithm that reads the price of a product and shows its new price, with a 5% discount

value = float(input('Enter the product's value: R$'))
discount = value*0.95
print('The product costs R${:.2f} and applying the 5% discount it comes to R${:.2f}'.format(value, discount))
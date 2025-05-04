'''Create a program that calculates the amount to be paid for a product, considering its normal price and payment conditions:
- cash (money/check): 10% discount
- cash (card): 5% discount
- 2x on card: normal price
- 3x or more on card: 20% interest'''

product = float(input('Enter the product value: R$'))
if product < 0:
    print('Invalid Value.')
    exit()
payment = int(input('''\n1 - cash (money/check)\n2 - cash (card)\n3 - up to 2x on card\n4 - 3x or more on card\nChoose payment option:'''))

if payment == 1:
    product *= 0.9
    print(f'Paying in cash (money/check), the product receives a 10% discount and costs R${product:.2f}')
elif payment == 2:
    product *= 0.95
    print(f'Paying in cash (card), the value of the product receives a 5% discount and costs R${product:.2f}')
elif payment == 3:
    installment = product/2
    print(f'Paying in 2x on the card each installment is R${installment:.2f}, totaling R${product:.2f}')
elif payment == 4:
    product *= 1.2
    installment = int(input('How many installments do you want to pay in? '))
    if installment >= 3:
        value = product/installment
        print(f'Paying in {installment} installments on the card, the value of the product receives 20% interest. Each installment will cost R${value:.2f}, totaling R$ {product:.2f}')
    else:
        print('Invalid Installment.')
else: 
    print('Invalid Option.')
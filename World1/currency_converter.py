#Create a program that reads how much a person has in their wallet and shows how many dollars they can buy

wallet=float(input('Enter how many reais you have in your wallet: R$'))
dollar = wallet/5.5
print('With R${:.2f}, you can buy US${:.2f}'.format(wallet,dollar))
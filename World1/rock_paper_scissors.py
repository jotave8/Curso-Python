#Create a program that makes the computer play Jokenpô with you

import random

user = int(input('[1] ROCK\n[2] PAPER\n[3] SCISSORS\nChoice: '))
if user > 3 or user < 1:
    print('Invalid Option.')
else:
    if user == 1:
        user = 'ROCK'
    elif user == 2:
        user = 'PAPER'
    else:
        user = 'SCISSORS'
    
    computer = ["ROCK","PAPER","SCISSORS"]
    computer = random.choice(computer)
    if computer == user :
        print(f"The computer chose {computer} and you chose {user}. It's a tie!")
    elif (user == 'ROCK' and computer == 'SCISSORS') or (user == 'PAPER' and computer == 'ROCK') or (user == 'SCISSORS' and computer == 'PAPER') :
        print(f'The computer chose {computer} and you chose {user}. You won!')
    else:
        print(f'The computer chose {computer} and you chose {user}. The computer won.')

import random

symbols = ['rock', 'paper', 'scissors']

player_wins = 0
computer_wins = 0

while max([player_wins, computer_wins]) < 3:
    player_symbol = None
    while player_symbol is None:
        input_symbol = input("What symbol do you want? ")
        if input_symbol in symbols:
            player_symbol = input_symbol
        else:
            print('Please pick rock, paper, or scissors.')

    computer_symbol = random.choice(symbols)

    print('Player: ', player_symbol)
    print('Computer: ', computer_symbol)

    if player_symbol == computer_symbol:
        print('Tie!')
    elif player_symbol == 'rock':
        if computer_symbol == 'paper':
            print('computer wins!')
            computer_wins += 1
        else:
            print('player wins!')
            player_wins += 1
    elif player_symbol == 'paper':
        if computer_symbol == 'scissors':
            print('computer wins!')
            computer_wins += 1
        else:
            print('player wins!')
            player_wins += 1
    elif player_symbol == 'scissors':
        if computer_symbol == 'rock':
            print('computer wins!')
            computer_wins += 1
        else:
            print('player wins!')
            player_wins += 1
print('player wins!: ')
print(player_wins)
print('computer wins!: ')
print(computer_wins)
    


    

import random
symbols = ['rock', 'paper', 'scissors']
player_wins = 0
computer_wins = 0
while max([player_wins, computer_wins])<3:
    player_symbol = None
    while player_symbol is None:
        input_symbol = input("What symbol do you want? ")
        if input_symbol in symbols:
            player_symbol = input_symbol
        else:
            print('Please rock paper or scissors')

    computer_symbol = random.choice(symbols)
    
    print('player:', player_symbol)
    print('computer:', computer_symbol)
          

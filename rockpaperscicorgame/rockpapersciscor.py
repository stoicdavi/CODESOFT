import random as rd
options = ('paper', 'rock', 'scissor')
def get_players_choice():
    player_choice = input("Choose an options (paper, rock or scissor): ").lower()
    while player_choice not in options:
        player_choice = input('Invalid choice! Please enter (paper, rock or scissor): ')
    return player_choice

computer = rd.choice(options)
print(f'Player choice: {get_players_choice()}')
print(f'Computers choice: {computer}')
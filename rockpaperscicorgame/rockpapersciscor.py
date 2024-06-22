import random as rd
options = ('paper', 'rock', 'scissor')
def get_players_choice():
    player_choice = input("Choose an options (paper, rock or scissor): ").lower()
    while player_choice not in options:
        player_choice = input('Invalid choice! Please enter (paper, rock or scissor): ')
    return player_choice

def computers_selection():
    return  rd.choice(options)

def determine_winner(player_choice, computer_choice):
    if  (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice== "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player"
    elif player_choice == computer_choice:
        return 'Tie'
    else:
        return 'Computer'

computer_choice = computers_selection()
player_choice = get_players_choice()
print(f'The winner is : {determine_winner(player_choice, computer_choice)}')
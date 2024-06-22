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
    
def return_Winner():

    computer_choice = computers_selection()
    player_choice = get_players_choice()
    winner = determine_winner(player_choice, computer_choice)
    print(f'Computers choice:  {computer_choice} \nUsers Choice: {player_choice}')
    return winner
  

def main():
    computer_score = 0
    player_score = 0
    while True:
        print('\n***Welcome to our DeanTech Paper, Rock, Scissor game! **')
        winner = return_Winner()
        if winner == 'Player':
            player_score += 1
            print("Congratulations! You won!")
        elif winner == 'Computer':
            print('You lose!')
            computer_score += 1
        else:
            print('It is a tie!')
            
        print(f"\n****Current scores****\nComputer: {computer_score}\nUser score: {player_score}")

        choice = input('Would you like to play again? ').lower()
        if choice not in ['yes', 'y']:
            break
  
    print(f'\n***The final scores are:**\nComputer scored: {computer_score}\nYou scored: {player_score}')
    if player_score > computer_score:
        print('You player won!')
    elif player_score < computer_score:
        print('You lose')
    else:
        print('It is a tie')

if __name__ == '__main__':
    main()

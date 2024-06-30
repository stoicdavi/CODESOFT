import random as rd

options = ('paper', 'rock', 'scissors')

def get_players_choice():
    player_choice = input("Choose an option (paper, rock, or scissors): ").lower()
    while player_choice not in options:
        player_choice = input('Invalid choice! Please enter (paper, rock, or scissors): ').lower()
    return player_choice

def computers_selection():
    return rd.choice(options)

def determine_winner(player_choice, computer_choice):
    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "scissors" and computer_choice == "paper") or \
       (player_choice == "paper" and computer_choice == "rock"):
        return "Player"
    elif player_choice == computer_choice:
        return 'Tie'
    else:
        return 'Computer'
def return_winner():
    computer_choice = computers_selection()
    player_choice = get_players_choice()
    winner = determine_winner(player_choice, computer_choice)
    print(f'Computer\'s choice: {computer_choice} \nPlayer\'s choice: {player_choice}')
    return winner
def main():
    computer_score = 0
    player_score = 0
    print('\n*** Welcome to our DeanTech Rock, Paper, Scissors game! ***')

    while True:
        print('\n*** The game is about to start! ***\nSelect:\n1. Start the game\n2. Exit the game\n')
        choice = input('Enter your choice: ')
        if choice == '2':
            break
        elif choice != '1':
            print('Invalid choice! Please enter 1 to start the game or 2 to exit the game')
            continue

        winner = return_winner()
        if winner == 'Player':
            player_score += 1
            print("Congratulations! You won!")
        elif winner == 'Computer':
            computer_score += 1
            print('You lose!')
        else:
            print('It is a tie!')

        print(f"\n**** Current scores ****\nComputer: {computer_score}\nPlayer: {player_score}")
        if input('Would you like to play again? (yes or no): ').lower() not in ['yes', 'y']:
            break

    print(f'\n*** Final scores ***\nComputer: {computer_score}\nPlayer: {player_score}')
    if player_score > computer_score:
        print('Congratulations! You won the game!')
    elif player_score < computer_score:
        print('You lost the game!')
    else:
        print('It\'s a tie!')



if __name__ == '__main__':
    main()

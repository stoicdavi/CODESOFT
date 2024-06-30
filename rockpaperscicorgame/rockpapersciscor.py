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

def main():
    total_computer_score = 0
    total_player_score = 0
    played_once = False

    print('\n*** Welcome to DeanTech Rock, Paper, Scissors! ***')

    while True:
        if played_once:
            print('\n**** Menu ****')
            print('1. Play again')
            print('2. Reset scores')
            print('3. Exit')

            choice = input('Enter your choice: ')
            if choice == '2':
                total_computer_score, total_player_score = 0, 0
                print('Scores have been reset.')
                continue
            elif choice == '3':
                break
            elif choice != '1':
                print('Invalid choice! Please select 1, 2, or 3.')
                continue

        player_choice = get_players_choice()
        computer_choice = computers_selection()
        winner = determine_winner(player_choice, computer_choice)
        print(f'\nComputer\'s choice: {computer_choice}\nPlayer\'s choice: {player_choice}')

        if winner == 'Player':
            total_player_score += 1
            print("Congratulations! You won!")
        elif winner == 'Computer':
            total_computer_score += 1
            print('You lose!')
        else:
            print('It\'s a tie!')

        print(f"\n**** Current scores ****\nComputer: {total_computer_score}\nPlayer: {total_player_score}")
        played_once = True

    print(f'\n*** Final scores ***\nComputer: {total_computer_score}\nPlayer: {total_player_score}')
    if total_player_score > total_computer_score:
        print('Congratulations! You won the game!')
    elif total_player_score < total_computer_score:
        print('You lost the game!')
    else:
        print('It\'s a tie!')

if __name__ == '__main__':
    main()

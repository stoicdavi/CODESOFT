import random as rd

options = ('paper', 'rock', 'sciscor')

player = input("Choose an options (paper, rock or sciscor): ")
computer = rd.choice(options)

print(f'Player choice: {player}')
print(f'Computers choice: {computer}')
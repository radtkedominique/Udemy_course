'''
import random
com = random.choice(['Rock', 'Paper', 'Scissors'])
player = input('Rock, Paper, Scissors? ')

while player != 'Rock' and player != 'Paper' and player != 'Scissors':
    player = input('Invalid! Please enter Rock, Paper or Scissors: ')

print(f'Com: {com}')
if player == com:
    print('You tie!')

if player == 'Rock' and com == 'Scissors':
    print('You win!')

elif player == 'Rock' and com == 'Paper':
    print('You loose!')

elif player == 'Paper' and com == 'Scissors':
    print('You loose!')

elif player == 'Paper' and com == 'Rock':
    print('You win!')

elif player == 'Scissors' and com == 'Rock':
    print('You loose!')

elif player == 'Scissors' and com == 'Paper':
    print('You win!')
'''

#use while loop to play until you win
import random
com_wins = 0
player_wins = 0

while True:
    state = ''
    player = input('Rock, Paper, Scissors? ')
    com = random.choice(['Rock', 'Paper', 'Scissors'])

    while player != 'Rock' and player != 'Paper' and player != 'Scissors':
        player = input('Invalid! Please enter Rock, Paper or Scissors: ')

    print(f'Com: {com}')
    if player == com:
        state = 'tie'

    elif player == 'Rock' and com == 'Scissors':
        state = 'win'

    elif player == 'Rock' and com == 'Paper':
        state = 'loose'

    elif player == 'Paper' and com == 'Scissors':
        state = 'loose'

    elif player == 'Paper' and com == 'Rock':
        state = 'win'

    elif player == 'Scissors' and com == 'Rock':
        state = 'loose'

    elif player == 'Scissors' and com == 'Paper':
        state = 'win'

    print(f'You {state}.')

    if state == 'win':
        player_wins += 1
    elif state == 'loose':
        com_wins += 1

    print('Player score:', player_wins)
    print('Com score:', com_wins)

    answer = input('Would you like to play again? (y/n): ')
    if answer.lower() == 'n':
        print('Player score:', player_wins)
        print('Com score:', com_wins)

        if player_wins > com_wins:
            print('You won!')
        elif com_wins > player_wins:
            print('You loose!')
        else:
            print('Draw!')

        print('Thank you for playing!')
        break



import random


all_possible_options = ['Rock','Paper','Scissors']
cpu_action = random.choice(all_possible_options)
user_input = input('Enter an option(R, P, or S): \n')

while True:
    if(user_input == 'R'):
        user_input = 'Rock'
    elif(user_input == 'P'):
        user_input = 'Paper'
    elif(user_input == 'S'):
        user_input = 'Scissors'
    elif(user_input not in all_possible_options):
        print('Error: invalid input')
        user_input = input('Enter an option(R, P, or S): \n')

    elif(user_input == cpu_action):
        print(f'Player({user_input}: CPU({cpu_action})')
        print(f'Both players selected {user_input}, thus, it is a tie!')
        print("Play again")
        cpu_action = random.choice(all_possible_options)
        user_input = input('Enter an option(R, P, or S): \n')
        continue
    else:
        print(f'Player({user_input}: CPU({cpu_action})')

        if(user_input == 'Rock'):
            if(cpu_action == 'Scissors'):
                print('Rock smashes scissors! You win!')
            else:
                print('Paper covers rock! You loose!')

        elif(user_input == 'Paper'):
            if(cpu_action == 'Rock'):
                print('Paper covers Rock! You win!')
            else:
                print('Scissors cuts paper! You lose!')

        elif(user_input == 'Scissors'):
            if(cpu_action == 'Paper'):
                print('Scissors cuts paper! You win!')
            else:
                print('Rock smashes scissors! You lose!')
        print("Game Over!")
        break



import random

options = {
    1: '✊',
    2: '✋',
    3: '✌️'
}

print('=========================')
print('Piedra Papel o Tijeras')
print('========================= \n')

print('1: ✊')
print('2: ✋')
print('3: ✌️ \n')


player = int(input('Por favor elige un numero \n'))

if player not in [1,2,3]:
    print('Solo se permite del 1 al 3')
else:
    computer = random.randint(1,3)
    print(f'Player saco: {options[player]}')
    print(f'Computer saco: {options[computer]}')

    if player == computer:
        print('Es un empate')
    elif (
        player == 1 and computer == 3 or
        player == 2 and computer == 1 or
        player == 3 and computer == 2

    ):
     print('Player Gano!!')
    else:
       print('Computer Gana')





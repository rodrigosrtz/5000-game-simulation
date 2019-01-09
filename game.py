#Game 5000!
#Playing version for humans!

from players import *
import time

print('=========================================\n\n Game 5000! \n\n=========================================\n\n')

total_players = []

print('...How many human players?')
humans = int(input())
for i in range(humans):
    print('Enter Player n.' + str(i+1) + "'s name:")
    n = input()
    total_players.append(Player(n, 'real', 0))
    print('\n-->' + str(total_players[i].name), 'joined the game!\n\n')

print('...How many Bots?')
bots = int(input())
for i in range(bots):
    print('Set the stop value for Bot n.' + str(i+1) + '\n(200 / 300 / 400 / ... )')
    s = int(input())
    n = 'Bot n.' + str(i+1)
    total_players.append(Player(n, 'bot', s))
    print('\n-->' + n, 'joined the game!\n\n')


print('\n\n\n...Loading the Game!...\n\n\n')
time.sleep(2)

loop = 0
again = 'n'
while True:
    print('---------------->', total_players[loop].name, "it's your turn!\n")
    time.sleep(1)
    total_players[loop].play()
    print('\n=================================')
    for i in total_players:
        print('Total points of', str(i.name) + ':', i.total_points)
    print('=================================\n\n\n')
    if total_players[loop].total_points == 5000:
        print('---------------->', total_players[loop].name, 'IS THE WINNER!!! <----------------')
        print('\n\nPLAY AGAIN?! [y/n]')
        again = input()
        if again == 'y' or again == 'Y':
            for i in total_players:
                i.total_points = 0
        else:
            break
    if loop < len(total_players) - 1:
        loop += 1
    else:
        loop = 0

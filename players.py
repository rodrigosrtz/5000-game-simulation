from random import choices
from dices import *
import time

class Player:
    """
    Class for creating players to join the simulation
    """
    def __init__(self, name, type, stop_value, play_points=0, turn_points=0, total_points=0):
        """
        Constructor

        :name: name of the player
        :type: 'real' for real players // 'bot' for bot players
        :stop_value: 200 // 300 // 400 // 500 // ... // 0 for manual_play
        """

        self.name = name
        self.type = type
        self.stop_value = stop_value
        self.play_points = play_points
        self.turn_points = turn_points
        self.total_points = total_points


    def play(self):
        if self.type == 'real':
            self.manual_play()
        else:
            self.bot_play()


    def manual_play(self):
        first_dice = 0
        second_dice = 0
        third_dice = 0
        self.turn_points = 0
        self.play_points = 0
        keep = 'y'
        while True:
            print('\nRolling the dices...')
            time.sleep(1)
            first_dice = choices([1, 2, 3, 4, 5, 6])[0]
            dice_side(first_dice)
            second_dice = choices([1, 2, 3, 4, 5, 6])[0]
            dice_side(second_dice)
            third_dice = choices([1, 2, 3, 4, 5, 6])[0]
            dice_side(third_dice)
            self.play_points = dice_points(first_dice, second_dice, third_dice)
            print('You scored in this play:', self.play_points)
            if self.play_points == 0:
                print('\nYou lost all the points of this turn!')
                time.sleep(1)
                self.turn_points = 0
                break
            if self.total_points + self.turn_points + self.play_points > 5000:
                print('Current Total Points:', self.total_points + self.turn_points + self.play_points)
                print('Ops, you outscored!\nYou lost all the points of this turn!')
                time.sleep(2)
                self.turn_points = 0
                break
            self.turn_points += self.play_points
            print('Total Turn Points:', self.turn_points)
            time.sleep(1)
            if self.total_points + self.turn_points == 5000:
                self.total_points += self.turn_points
                break
            if self.turn_points % 100 != 0:
                print("\nYou can't stop playing!")
            else:
                print('\nKEEP TRYING TO SCORE?? [y/n]')
                keep = input()
                if keep == 'n' or keep == 'N':
                    print('Writing down your points...')
                    self.total_points += self.turn_points
                    break


    def bot_play(self):
        num = self.stop_value
        first_dice = 0
        second_dice = 0
        third_dice = 0
        self.turn_points = 0
        self.play_points = 0
        while self.turn_points < num or self.turn_points % 100 != 0:
            print('\nRolling the dices...')
            time.sleep(1)
            first_dice = choices([1, 2, 3, 4, 5, 6])[0]
            dice_side(first_dice)
            second_dice = choices([1, 2, 3, 4, 5, 6])[0]
            dice_side(second_dice)
            third_dice = choices([1, 2, 3, 4, 5, 6])[0]
            dice_side(third_dice)
            self.play_points = dice_points(first_dice, second_dice, third_dice)
            print('You scored in this play:', self.play_points)
            if self.play_points == 0:
                print('\nYou lost all the points of this turn!')
                self.turn_points = 0
                break
            if self.total_points + self.turn_points + self.play_points > 5000:
                print('Current Total Points:', self.total_points + self.turn_points + self.play_points)
                print('Ops, you outscored!\nYou lost all the points of this turn!')
                self.turn_points = 0
                break
            self.turn_points += self.play_points
            if self.total_points + self.turn_points == 5000:
                break
        self.total_points += self.turn_points

# 5000-game-simulation
Python simulation for the game 5000!

### Rules
Objective: First player to score 5000, wins!

Play with 3 dices:
    value 1 = 100 points
    value 5 = 50 points
    3 dices with the same value (111, 222, 333, ...) = 1000 points
    any other value = no points

How to play:
Each player has their turn;
In a turn, a player can play 'n' times to score points:
    After a play, we look at the dices and the player decides if she wants to:
        1. Stop, write down the points of this turn and pass the dices (pass the turn);
        2. Keep trying to score more points;

        if she gets a dice combination without 1 or 5 or three equal values,
            she loses all points of this turn and has to pass the dices to the next player

        if her sum score of this turn is not divisible by 100 (i.e. 50, 150, 250, ...),
            she has to keep playing

        if her total score becomes bigger than 5000,
            she loses all points of this turn and has to pass the dices to the next player


It happens to be a variation of a game called Farkle
https://en.wikipedia.org/wiki/Farkle


# !/usr/bin/env python3
import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    round_count = 0

    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        return 'rock'

    def learn(self, move1):
        pass

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def valid_input(self, prompt, options):
        """ this function ensures that all moves entered are valid,
        this is achieved by comparing moves entered to the global moves.
        Args:
        prompt: is the error message displayed.
        options: this is the move option entered.
        """
        while True:
            option = input(prompt).lower()
            if option in options:
                return option
            print(f'Sorry, wrong entry "{option}" .Try again!')


class RandomPlayer(Player):
    """ this player randomly select moves fron the global moves Variable"""

    def move(self):
        return random.choice(moves)


class Humanplayer(Player):
    """this play takes in input from the external player by,
    calling the validate function to ensure correct entry.
    """
    def move(self):
        human_move = self.valid_input("please enter Rock, paper, scissors : ",
                                      ["rock", "paper", "scissors"])
        return human_move


class CyclePlayer(Player):
    """ remembers the move in the last round and cycle through a new move """
    def __init__(self):
        super().__init__()

    def move(self):
        if self.my_move is None:
            self.my_move = moves[0]
            return self.my_move
        if self.my_move == moves[0]:
            self.my_move = moves[1]
            return self.my_move
        if self.my_move == moves[1]:
            self.my_move = moves[2]
            return self.my_move
        if self.my_move == moves[2]:
            self.my_move = moves[0]
            return self.my_move


class Reflectplayer(Player):
    def __init__(self):
        super().__init__()

        self.reflect_move = ""

    def move(self):
        if self.reflect_move == "":
            self.their_move = random.choice(moves)
            return self.their_move
        else:
            self.my_move = self.reflect_move
            return self.my_move

    def learn(self, move1):
        self.reflect_move = move1


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        # Default scores
        self.player_1_score = 0
        self.player_2_score = 0

    def Number_of_rounds(self):
        while True:
            self.round_number = input("enter number of rounds " +
                                      " or type quit to exit : ")
            if self.round_number.isdigit() == 1:
                return self.round_number
            elif self.round_number.isdigit() > 1:
                return self.round_number
            elif self.round_number == 'quit':
                exit()
            else:
                print("wrong input try again")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: ({move1}) Player 2: ({move2})")
        if self.beat(move1, move2):
            self.player_1_score += 1
            status = " *** palyer one wins this round***"

        elif move1 == move2:
            self.player_1_score = self.player_1_score
            self.player_2_score = self.player_2_score
            status = " *** this round is a draw *** "
        else:
            self.player_2_score += 1
            status = "**** player two wins this round **** "
        print(f"you played: ({move1})  opponet played : ({move2}) ",
              f" \n{status} ", f" \n your_scores is ({self.player_1_score})",
              f" opponet_scores is ({self.player_2_score}) ")

        self.p2.learn(move1)

    def final_outcome(self):
        if self.player_1_score == self.player_2_score:
            print("match draw")
        elif self.player_1_score > self.player_2_score:
            print("you win")
        elif self.player_1_score < self.player_2_score:
            print("opponet wins")

    def beat(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def final_score(self):
        print(f"final_score: ({self.player_1_score}), ({self.player_2_score})")

    def one_round(self):
        print(f"==========({self.round_number})========round is to be played")
        self.play_round()

    def multiple_round(self):
        print(f"({self.round_number}) rounds are going to be played")
        for round in range(int(self.round_number)):
            print(f"=========Round ({round +1}):============")
            self.play_round()

    def round_decision(self):
        if int(self.round_number) == 1:
            self.one_round()
        elif int(self.round_number) > int(1):
            self.multiple_round()

    def play_game(self):
        print("the Game has started!")
        self.Number_of_rounds()
        self.round_decision()
        self.final_score()
        self.final_outcome()
        print("end of the game!")


if __name__ == '__main__':
    players = random.choice([Reflectplayer(), RandomPlayer(), CyclePlayer()])
    game = Game(Humanplayer(), Reflectplayer())
    game.play_game()

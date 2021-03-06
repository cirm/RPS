import random
from RockPaperScissors.strings import Hand, Result
from RockPaperScissors.userInterface import CommandLineInterface


class RockPaperScissors(object):
    """used for main game flow"""

    def __init__(self):
        self.ui = CommandLineInterface()
        self.games = []       
        
    def start_new_game(self):
        state = True

        while state:
            player_hand = self.ui.read_input_hand()
            comp_hand = self.generate_computer_hand()
            outcome = self.pick_winner(player_hand, comp_hand)

            game = Game(player_hand, comp_hand, outcome)

            self.ui.declare_winner(player_hand, comp_hand, outcome)
            self.games.append(game)

            state = self.ask_next_action()

    @staticmethod
    def generate_computer_hand():
        comp_hand = random.choice([Hand.ROCK, Hand.PAPER, Hand.SCISSORS])
        return comp_hand

    @staticmethod
    def pick_winner(hand1, hand2):
        if hand1 == hand2:
            return Result.DRAW
        elif hand1 == Hand.ROCK and hand2 == Hand.SCISSORS:
            return Result.WIN
        elif hand1 == Hand.PAPER and hand2 == Hand.ROCK:
            return Result.WIN
        elif hand1 == Hand.SCISSORS and hand2 == Hand.PAPER:
            return Result.WIN
        else:
            return Result.LOSS
       
    def ask_next_action(self):
        state = self.ui.read_action()

        while state == "2":
            self.ui.display_history(self.games)
            state = self.ui.read_action()

        if state == "1":  # start new game
            return True
        else:  # quit
            return False


class Game(object):
    """ used for storing individual game objects"""

    def __init__(self, player_hand, computer_hand, winner):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.winner = winner

    def get_player_hand(self):
        return self.player_hand

    def get_comp_hand(self):
        return self.computer_hand

    def get_winner(self):
        return self.winner


if __name__ == "__main__":
    RockPaperScissors().start_new_game()
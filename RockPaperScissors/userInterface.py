from RockPaperScissors.strings import Hand, Action

__author__ = 'madis'


class CommandLineInterface(object):
    """used for reading and parsing the information"""

    @staticmethod
    def ask_hand():
        hand = input("Pick a hand (Rock, Paper, Scissors)?\n")
        return hand

    @staticmethod
    def ask_action():
        action = input("Please select: [1]Play another game, [2]View"
                           " scores or [3]Quit?")
        return action

    def read_input_hand(self):
        hand = self.ask_hand().title()
        while not (hand == Hand.ROCK or hand == Hand.PAPER or hand == Hand.SCISSORS):
            return self.read_input_hand()

        return hand

    def read_action(self):
        state = self.ask_action()
        while not (state == Action.NEW_GAME or state == Action.VIEW_SCORE or state == Action.QUIT):
            self.ask_action()

        return state

    @staticmethod
    def declare_winner(player, comp, outc):
        print ("You picked %s, computer picked %s and it's "
              "a %s for you!" % (player, comp, outc))

    @staticmethod
    def display_history(games_list):
        print ("You have played %s game(s):" % (len(games_list)))
        print ("Player".ljust(9) + "Computer".ljust(9) + "Winner".ljust(8))
        for game in games_list:
            print (game.get_player_hand().ljust(9) +
                   game.get_comp_hand().ljust(9) + game.get_winner())
from RockPaperScissors.Strings import Hand, Action

__author__ = 'madis'


class CommandLineInterface(object):
    '''used for reading and parsing the information'''
    def ask_hand(self):
        hand = input("Pick a hand (Rock, Paper, Scissors)?\n")
        return hand

    def ask_action(self):
        action = input("Please select: [1]Play another game, [2]View"
                           " scores or [3]Quit?")
        return action

    def read_input_hand(self):
        hand = self.ask_hand().title()
        if (hand == Hand.ROCK or hand == Hand.PAPER or hand == Hand.SCISSORS):
            return hand
        else:
            return self.read_input_hand()

    def read_action(self):
        state = self.ask_action()
        if (state == Action.NEW_GAME or state == Action.VIEW_SCORE or state == Action.QUIT):
            return state
        else:
            return self.read_action()

    def declare_winner(self, player, comp, outc):
        print ("You picked %s, computer picked %s and it's "
              "a %s for you!" % (player, comp, outc))

    def display_history(self, games_list):
        print ("You have played %s game(s):" % (len(games_list)))
        print ("Player".ljust(9) + "Computer".ljust(9) + "Winner".ljust(8))
        for game in games_list:
            print (game.get_player_hand().ljust(9) +
                   game.get_comp_hand().ljust(9) + game.get_winner())
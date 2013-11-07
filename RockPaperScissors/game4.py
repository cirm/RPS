from sys import exit
import random


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
       
        
class RockPaperScissors(object):       
    '''used for main game flow'''
    def __init__(self):
        self.userInterface = CommandLineInterface()
        self.games = []       
        
    def start_new_game(self):
        player_hand = self.userInterface.read_input_hand()
        comp_hand = self.generate_computer_hand()
        outcome = self.pick_winner(player_hand, comp_hand)

        game = Game(player_hand, comp_hand, outcome)

        self.userInterface.declare_winner(player_hand, comp_hand, outcome)
        self.games.append(game)

        self.ask_next_action()
           
    def generate_computer_hand(self):
        comp_hand = random.choice([Hand.ROCK, Hand.PAPER, Hand.SCISSORS])
        return comp_hand
        
    def pick_winner(self, hand1, hand2):
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
        state = self.userInterface.read_action()
        if state == "1":  # start new game
            self.start_new_game()
        elif state == "2":  # view history
            self.userInterface.display_history(self.games)
            self.ask_next_action()
        else:  # quit
            print("This was really nice!")
            exit(0)
                    
    
class Game(object):
    ''' used for storing individual game objects'''
    def __init__(self, player_hand, computer_hand, winner):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.winner = winner
                     
    def set_player_hand(self, hand):
        self.player_hand = hand

    def get_player_hand(self):
        return self.player_hand

    def set_computer_hand(self, hand):
        self.computer_hand = hand
        
    def set_winner(self, outcome):
        self.winner = outcome
        
    def get_comp_hand(self):
        return self.computer_hand
        
    def get_winner(self):
        return self.winner
    

class Hand(object):
    
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"


class Action(object):
    NEW_GAME = "1"
    VIEW_SCORE = "2"
    QUIT = "3"


class Result(object):
    DRAW = "Draw"
    WIN = "Win"
    LOSS = "Loss"
    
    
if __name__ == "__main__":
    RockPaperScissors().start_new_game()
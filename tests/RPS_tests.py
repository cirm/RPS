from nose.tools import *
import RPS.game4
import pexpect


def test_games_list():
        rps = RPS.game4.RockPaperScissors()
	eq_(rps.games, [])

def test_generator():
        rps = RPS.game4.RockPaperScissors()
	eq_(type(rps.generate_computer_hand()), type("str"))

def test_pick_winner():
        rps = RPS.game4.RockPaperScissors()
	eq_(rps.pick_winner(Hand.ROCK, Hand.PAPER), Result.LOSS)
	eq_(rps.pick_winner(Hand.ROCK, Hand.SCISSORS), Result.WIN)
	eq_(rps.pick_winner(Hand.ROCK, Hand.ROCK), Result.DRAW)
	eq_(rps.pick_winner(Hand.PAPER, Hand.PAPER), Result.DRAW)
	eq_(rps.pick_winner(Hand.PAPER, Hand.ROCK), Result.WIN)
	eq_(rps.pick_winner(Hand.PAPER, Hand.SCISSORS), Result.LOSS)
	eq_(rps.pick_winner(Hand.SCISSORS, Hand.SCISSORS), Result.DRAW)
	eq_(rps.pick_winner(Hand.SCISSORS, Hand.PAPER), Result.WIN)
	eq_(rps.pick_winner(Hand.SCISSORS, Hand.ROCK), Result.LOSS)

def test_Game_class():
    	rps = RPS.game4.RockPaperScissors()
	rps.game = RPS.game4.Game()
	
	rps.game.set_player_hand("1")
	rps.game.set_computer_hand("2")
	rps.game.set_winner("3")
	
	eq_(rps.game.get_player_hand(), "1")
	eq_(rps.game.get_comp_hand(), "2")
	eq_(rps.game.get_winner(), "3")

def test_ask_hand():
        ui = RPS.game4.CommandLineInterface()
        RPS.game4.raw_input = lambda _: "Rock"
        eq_(ui.ask_hand(), "Rock")
        
def test_ask_action():
        ui = RPS.game4.CommandLineInterface()
        RPS.game4.raw_input = lambda _: "1"
        eq_(ui.ask_action(), "1")

def test_integration():
        child = pexpect.spawn ("python ../Final_Jullinen/RPS/game4.py")
        child.expect ("Pick a")
        child.sendline ("Rock")
        child.expect ("Please select:")
        child.sendline ("1")
        child.expect ("Pick a")
        child.sendline ("Paper")
        child.expect ("Please select:")
        child.sendline ("3")


class Hand(object):

	ROCK = "Rock"
	PAPER = "Paper"
	SCISSORS = "Scissors"


class Result(object):
	
	DRAW = "Draw"
	WIN = "Win"
	LOSS = "Loss"
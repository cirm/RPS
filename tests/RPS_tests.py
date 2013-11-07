from nose.tools import *
import RockPaperScissors.Engine
import pexpect


def test_games_list():
    rps = RockPaperScissors.Engine.RockPaperScissors()
    eq_(rps.games, [])


def test_generator():
    rps = RockPaperScissors.Engine.RockPaperScissors()
    eq_(type(rps.generate_computer_hand()), type("str"))


def test_pick_winner():
    rps = RockPaperScissors.Engine.RockPaperScissors()
    eq_(rps.pick_winner(Hand.ROCK, Hand.PAPER), Result.LOSS)
    eq_(rps.pick_winner(Hand.ROCK, Hand.SCISSORS), Result.WIN)
    eq_(rps.pick_winner(Hand.ROCK, Hand.ROCK), Result.DRAW)
    eq_(rps.pick_winner(Hand.PAPER, Hand.PAPER), Result.DRAW)
    eq_(rps.pick_winner(Hand.PAPER, Hand.ROCK), Result.WIN)
    eq_(rps.pick_winner(Hand.PAPER, Hand.SCISSORS), Result.LOSS)
    eq_(rps.pick_winner(Hand.SCISSORS, Hand.SCISSORS), Result.DRAW)
    eq_(rps.pick_winner(Hand.SCISSORS, Hand.PAPER), Result.WIN)
    eq_(rps.pick_winner(Hand.SCISSORS, Hand.ROCK), Result.LOSS)


def test_game_class():
    rps = RockPaperScissors.Engine.RockPaperScissors()
    rps.game = rps.Engine.Game()

    rps.game(player_hand = "1", computer_hand = "2", winner = "3")

    eq_(rps.game.get_player_hand(), "1")
    eq_(rps.game.get_comp_hand(), "2")
    eq_(rps.game.get_winner(), "3")


def test_ask_hand():
    ui = RockPaperScissors.Engine.CommandLineInterface()
    RockPaperScissors.Engine.input = lambda _: "Rock"
    eq_(ui.ask_hand(), "Rock")


def test_ask_action():
    ui = RockPaperScissors.Engine.CommandLineInterface()
    RockPaperScissors.Engine.raw_input = lambda _: "1"
    eq_(ui.ask_action(), "1")


def test_integration():
    child = pexpect.spawn("python ../RPS/RockPaperScissors/Engine.py")
    child.expect("Pick a")
    child.sendline("Rock")
    child.expect("Please select:")
    child.sendline("1")
    child.expect("Pick a")
    child.sendline("Paper")
    child.expect("Please select:")
    child.sendline("3")


class Hand(object):

    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"


class Result(object):

    DRAW = "Draw"
    WIN = "Win"
    LOSS = "Loss"

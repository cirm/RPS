from nose.tools import *
import RockPaperScissors.engine
import RockPaperScissors.userInterface


def test_games_list():
    rps = RockPaperScissors.engine.RockPaperScissors()
    eq_(rps.games, [])


def test_generator():
    rps = RockPaperScissors.engine.RockPaperScissors()
    eq_(type(rps.generate_computer_hand()), type("str"))


def test_pick_winner():
    rps = RockPaperScissors.engine.RockPaperScissors()
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
    rps = RockPaperScissors.engine.Game(player_hand="1", computer_hand="2", winner="3")

    eq_(rps.get_player_hand(), "1")
    eq_(rps.get_comp_hand(), "2")
    eq_(rps.get_winner(), "3")


def test_ask_hand():
    ui = RockPaperScissors.engine.CommandLineInterface()
    RockPaperScissors.userInterface.input = lambda _: "Rock"
    eq_(ui.ask_hand(), "Rock")


def test_ask_action():
    ui = RockPaperScissors.engine.CommandLineInterface()
    RockPaperScissors.userInterface.input = lambda _: "1"
    eq_(ui.read_action(), "1")


class Hand(object):

    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"


class Result(object):

    DRAW = "Draw"
    WIN = "Win"
    LOSS = "Loss"

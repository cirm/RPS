__author__ = 'madis'


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
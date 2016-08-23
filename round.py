"""Stores a single round"""

import time
from singles_score import SinglesScore
from player import Player



class Round:
    """Links together the various classes/information for one round"""
    def __init__(self):
        self.singles_round = SinglesScore()
        self.player = Player()  # stores user specific data that is mostly static
        self.date = time.strftime('%Y-%m-%d %H:%M:%S') # can be used to pull weather later
        self.starting_station = 1  # the default station is one, small detail only useful for statistics
        self.location = 'Portland Gun Club' # static for now, eventually will use the day class for this information

    def __eq__(self, other):
        return(
            self.singles_round == other.singles_round and
            self.player == other.player and
            self.date == other.date and
            self.starting_station == other.starting_station
        )

    def __repr__(self):
        return 'Round({!r}{!r}{!r}{!r})'.format(
            singles_round, player, date, starting_station
        )


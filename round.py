"""Stores a single round"""

import time
from singles_score import SinglesScore
from player import Player



class Round:
    """Links together the various classes/information for one round"""
    def __init__(self):
        self.singles_round = SinglesScore()
        self.player = Player()
        self.date = time.strftime('%Y-%m-%d %H:%M:%S')
        self.starting_station = 1
        # self.shotgun_shells = shotgun_shells
        # self.gun = gun
        # self.excuses = excuses

    def __eq__(self, other):
        return(
            self.singles_round == other.singles_round and
            self.player == other.player and
            self.date == other.date and
            self.starting_station == other.starting_station
            # self.shotgun_shells = other.shotgun_shells
            # self.gun = other.gun
            # self.excuses = other.excuses
        )

    def __repr__(self):
        return 'Round({!r}{!r}{!r}{!r})'.format(
            singles_round, player, date, starting_station
        )


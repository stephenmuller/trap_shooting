"""Stores a single round"""


class Round:
    """stores a single round of trap"""
    def __init__(self, player):
        self.singles_round = []
        self.player = player
        self.date = date
        self.starting_station = starting_station
        self.shotgun_shells = shotgun_shells
        self.gun = gun
        self.excuses = excuses

    def __eq__(self, other):
        self.singles_round = other.singles_round
        self.player = other.player
        self.date = other.date
        self.starting_station = other.starting_station
        self.shotgun_shells = other.shotgun_shells
        self.gun = other.gun
        self.excuses = other.excuses

    def __repr__(self):
        return 'Round({!r}{!r}{!r}{!r}{!r}{!r}{!r})'.format(
            singles_round, player, date, starting_station, shotgun_shells,
            gun, excuses
        )

def hit_miss(hit_or_miss):
    """Adds result of each shot to a list stored in a round class.

    Expects maybe to be a boolean.

    >>> a = Round('goober')
    >>> a.hit_miss(True)
    >>> a.hit_miss(False)
    >>> a
    """
    if hit_or_miss:
        self.singles_round.append([True])
    else:
        self.singles_round.append([False])

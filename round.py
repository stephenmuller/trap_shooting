"""Stores a single round"""


class Round:
    """Stores a single round of trap shooting"""
    def __init__(self):
        self.singles_round = []
        self.shotgun_shells = shotgun_shells
        self.starting_station = starting_station
        self.player_name = player_name
        self.date = date
        self.excuses = excuses

    # def __eq__(self, other):
    #     """implements equality
    #
    #     >>> a = Round()
    #     >>> b = Round()
    #     >>> a == b
    #     True
    #
    #     >>> a = Round([0, 1, 0, 1])
    #     >>> b = Round()
    #     >>> a == b
    #     False
    #     """
    #     return(
    #         self.singles_round == other.singles_round and
    #         self.shotgun_shells == other.shotgun_shells and
    #         self.starting_station = other.starting_station and
    #         self.player_name = other.player_name and
    #         self.date = other.date and
    #         self.excuses = other.excuses
    #     )

    def __repr__(self):
        """implements repr"""
        return 'Round({})'.format(singles_round)

def hit_miss(self, hit_or_miss):
    """Adds result of each shot to a list stored in a round class.

    Expects maybe to be a boolean.

    >>> a = Round()
    >>> a.hit_miss(True)
    >>> a.hit_miss(False)
    >>> a
    """
    if hit_or_miss:
        self.singles_round.append[True]
    else:
        self.singles_round.append[False]

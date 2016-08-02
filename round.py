"""Stores a single round"""


class Round:
    """Stores a single round of trap shooting"""
    def __init__(self):
        self.singles_round = []

    def __eq__(self, other):
        """implements equality

        >>> a = Round()
        >>> b = Round()
        >>> a == b
        True

        >>> a = Round([0, 1, 0, 1])
        >>> b = Round()
        >>> a == b
        False
        """
        return(
            self.singles_round == other.singles_round
        )

    def __repr__(self):
        """implements repr"""
        return 'Round({})'.format(singles_round)

    def hit_miss(self maybe):
        """Adds result of each shot to a list stored in a round class.

        Expects maybe to be a boolean.

        >>> a = Round()
        >>> a.hit_miss(hit)
        >>> a

        """
        if maybe:
            self.singles_round.append('hit')
        else:
            self.singles_round.append('miss')
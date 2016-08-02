"""Keeps track of a single round"""


class Round:
    """Stores a single round of trap shooting"""
    def __init__(self, singles_round):
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
        return 'Round({}, {})'.format(singles_round)


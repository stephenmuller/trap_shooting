"""A basic class that holds the default value for one round of 25 targets. By default they're all set to true"""

class SinglesScore:
    """score"""
    def __init__(self):
        self.score = [
            True, True, True, True, True,
            True, True, True, True, True,
            True, True, True, True, True,
            True, True, True, True, True,
            True, True, True, True, True
        ]

    def __eq__(self, other):
        return (self.score == other.score)

    def __repr__(self):
        return 'Score({})'.format(self.score)

    def score_as_int(self):
        """Takes the boolean score and returns an integer value

        >>> a = SinglesScore()
        >>> a.score_as_int()
        25
        """
        return self.score.count(True)

    def missed_target(self, target_number):
        """For setting a value to false

        >>> a = SinglesScore()
        >>> a.missed_target(24)
        >>> print(a.score)
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False]
        """
        self.score[target_number] = False

    def station_score(self, score_out_of_five, station):
        """

        :param score_out_of_five: int value between 1 and 5 representing the score at a station, assumed
        :param station: station shot from, 
        :return:
        """
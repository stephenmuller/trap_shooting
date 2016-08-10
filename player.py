"""A class for storing basic player information

'gun' will eventually be a class for storing things like make/model, barrel information, chokes etc.
"""

class Player:

    def __init__(self, name):
        self.name = name
        self.gun = 'gun placeholder'

    def __eq__(self, other):
        """eq"""
        Return ( self.name == other.name and self.gun == other.gun)

    def __repr__(self):
        """repr"""
        return 'Player({},{}'.format(self.name, self.gun)
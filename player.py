"""Stores all the information about a player"""

from round import Round


class Player:

    def __init__(self, name, rounds):
        self.name = name
        self.rounds = []
        self.info = info

    def __eq__(self, other):
        """eq"""
        self.name = other.name
        self.rounds = other.rounds
        self.info = other.info

    def __repr__(self):
        """repr"""
        return'Player({},{},{},'
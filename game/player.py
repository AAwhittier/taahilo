from game.score import Score


class Player:
    """Card inside of a deck or game.

    Controls the behaviour of an individual card.

    Attributes:

    """

    def __init__(self, score):
        """Constructs a new Player.

        Controls the actions of a player.

        Args:
            self (Player): an instance of Card.
            score (int): The score of the player.
        """
        self.score = Score(score)
        self.guess = ''

    def set_guess(self, guess):
        """Modifys the value of the players guess.

        Args:
            self (Player): An instance of Director.
            guess (char): Value guessed by the player.
        """
        self.guess = guess

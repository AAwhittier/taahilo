class Score:
    """Card inside of a deck or game.

    Controls the behaviour of an individual card.

    Attributes:

    """

    def __init__(self, current_score):
        """Constructs a new Score.

        Controls the value of a score.

        Args:
            self (Card): an instance of Card.
            current_score (int): The current score to begin with.
        """
        self.current_score = current_score

    def adjust_score(self, adjustment):
        """Modifys the score based on adjusment.

        Args:
            self (Score): An instance of Director.
            adjustment (int): Value to change the score by.
        """
        self.current_score += adjustment

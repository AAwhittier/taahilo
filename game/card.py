class Card:
    """Card inside of a deck or game.

    Controls the behaviour of an individual card.

    Attributes:

    """

    def __init__(self, number):
        """Constructs a new Card.

        Controls the value of a single card.

        Args:
            self (Card): an instance of Card.
            number (int): Face value of the card.
        """
        self.number = number

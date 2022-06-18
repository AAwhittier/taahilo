from game.card import Card
import random


class Deck:
    """A deck of cards.

    Controls the behaviour of a deck containing multiple cards.

    Attributes:

    """

    def __init__(self, deck_size):
        """Constructs a new Deck.

        Controls a deck of playing card of dexk_size size.

        Args:
            self (Deck): an instance of Deck.
            deck_size (int): The size of the deck.
        """
        self.deck_size = deck_size
        self.cards = list()

        for i in range(deck_size):
            self.cards.append(Card(i))

    def shuffle(self):
        """Randomly rearranges the order of the deck.

        Args:
            self (Deck): An instance of Director.
        """
        random.shuffle(self.cards)

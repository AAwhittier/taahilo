from game.deck import Deck
from game.player import Player


class Director:
    """A deck of cards.

    Controls the behaviour of a deck containing multiple cards.

    Attributes:

    """

    def __init__(self, deck_size):
        """Constructs a new Director.

        Controls the flow of play for the Hilo game.

        Args:
            self (Director): an instance of Deck.
            deck_size (int): How large of a deck to begin the game with.
        """
        self.deck = Deck(deck_size)
        self.deck.shuffle()

        self.player = Player(300)

    def get_input(self, possible_values, message, retry_message):
        """Obtain user input, printing a request messate and a message
        to retry if the values are not allowed.

        Args:
            self (Director): An instance of Director.
            possible_values (list()): Legal values for the input to be.
            message (string): Request to the user / prompt.
            retry_message (string): Error message if the value is not allowed.
        """

        value = ''
        while value not in possible_values:
            value = input(message)

            if value not in possible_values:
                print(retry_message)

        return value

    def compare_guess_to_deck(self, card_number):
        """Compares the users guess to the deck values to determine if they were correct.

        Args:
            self (Director): An instance of Director.
            card_number (int): Number of the card being compared.
        """

        if self.player.guess == 'h' and self.deck.cards[card_number].number < self.deck.cards[card_number+1].number:
            return True
        elif self.player.guess == 'l' and self.deck.cards[card_number].number > self.deck.cards[card_number+1].number:
            return True
        else:
            return False

    def play_game(self):
        """Flow control for the game. Handles i/o and decision making.

        Args:
            self (Director): An instance of Director.
        """
        turn_count = 0
        is_playing = True
        current_card = 0

        # Core game loop.
        while turn_count < self.deck.deck_size \
                and is_playing \
                and self.player.score.current_score > -1:

            # Check current card.
            print(f"The card is: {self.deck.cards[current_card].number}")

            # Obtain users guess.
            self.player.set_guess(self.get_input(['h', 'l'], "Higher or lower? [h/l]: ", "Value must be 'h' or 'l'. "))

            # Check next card in deck.
            print(f"Next card was: {self.deck.cards[current_card+1].number}")

            # Move the players score based on if their guess was correct.
            if self.compare_guess_to_deck(current_card):
                self.player.score.adjust_score(100)
            else:
                self.player.score.adjust_score(-75)

            print(f"Your score is: {self.player.score.current_score}")

            # End game if input is 'n'.
            play_again = self.get_input(['y', 'n'], "Play again? ", "Value must be 'h' or 'l'. ")
            if play_again == 'n':
                is_playing = False

            # Move to the next card.
            current_card += 1
            print()



from enum import Enum
from generic_deck import Card, Deck, DeckBuilder

class Suit(Enum):
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3

class BlackJackCard(Card):
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit
    
    @property
    def suit(self):
        return self._suit

class BlackJackDeck(Deck):
    pass

class BlackJackDeckBuilder:
    def create_deck(self):
        deck = BlackJackDeck()
        suits = [Suit.SPADES,
        Suit.HEARTS,
        Suit.DIAMONDS,
        Suit.CLUBS
        ]
        for suit in suits:
            for value in range(1,14):
                deck.add_card(BlackJackCard(value, suit))
            
        return deck




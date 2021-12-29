from random import shuffle

class Card:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value

class Deck:
    def __init__(self):
        self._cards = []

    @property
    def is_empty(self):
        return not self._cards

    @property
    def remaining_cards(self):
        return len(self._cards)

    def add_card(self, card):
        self._cards.append(card)

    def draw_card(self):
        return self._cards.pop()
    
    def shuffle(self):
        shuffle(self._cards)

class DeckBuilder:
    
    def create_deck(self,values):
        deck = Deck()
        for value in values:
            deck.add_card(Card(value))
        
        return deck

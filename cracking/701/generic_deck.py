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
    def __init__(self):
        pass
    
    def create_deck(self,values):
        your_brand_new_fancy_deck = Deck()
        for value in values:
            your_brand_new_fancy_deck.add_card(Card(value))
        
        return your_brand_new_fancy_deck

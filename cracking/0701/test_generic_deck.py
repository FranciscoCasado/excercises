import unittest
from generic_deck import Card, Deck, DeckBuilder


class TestDeck(unittest.TestCase):
    def test_empty_deck(self):
        d = Deck()
        self.assertTrue(d.is_empty)

    def test_non_empty_deck(self):
        d = Deck()
        for i in range(10):
            c = Card(i)
            d.add_card(c)
        self.assertFalse(d.is_empty)
        self.assertEqual(d.remaining_cards, 10)

    def test_draw_card_deck(self):
        d = Deck()
        for i in range(10):
            c = Card(i)
            d.add_card(c)

        self.assertEqual(d.draw_card().value, 9)
        self.assertEqual(d.remaining_cards, 9)

class TestDeckBuilder(unittest.TestCase):
    def test_create_deck(self):
        b = DeckBuilder()
        d = b.create_deck(range(10))
        self.assertFalse(d.is_empty)
        self.assertEqual(d.remaining_cards, 10)
        self.assertEqual(d.draw_card().value, 9)
        self.assertEqual(d.remaining_cards, 9)


if __name__ == '__main__':
    unittest.main()

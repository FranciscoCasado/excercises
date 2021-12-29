import unittest
from deck import Card, Deck


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

        d.draw_card()
        self.assertEqual(d.remaining_cards, 9)


if __name__ == '__main__':
    unittest.main()

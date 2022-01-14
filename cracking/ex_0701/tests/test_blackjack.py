import unittest
from cracking.ex_0701.blackjack import BlackJackCard, BlackJackDeck, BlackJackDeckBuilder, Suit



class TestBlackJackDeck(unittest.TestCase):
    def test_create_deck(self):
        d = BlackJackDeckBuilder().create_deck()
        self.assertFalse(d.is_empty)
        self.assertEqual(d.remaining_cards, 52)

    def test_draw_card(self):
        d = BlackJackDeckBuilder().create_deck()
        c = d.draw_card()
        self.assertEqual(c.value, 13)
        self.assertEqual(c.suit, Suit.CLUBS)
        self.assertEqual(d.remaining_cards, 51)



if __name__ == '__main__':
    unittest.main()

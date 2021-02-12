import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()

    def test_check_for_ace(self):
        card = Card("hearts", 1)
        self.assertEqual(True, self.card_game.check_for_ace(card))

    def test_highest_card(self):
        card1 = Card("spades", 9)
        card2 = Card("hearts", 2)
        self.assertEqual(card1, self.card_game.highest_card(card1, card2))

    def test_cards_total(self):
        card1 = Card("spades", 9)
        card2 = Card("hearts", 2)
        cards = (card1, card2)
        self.assertEqual("You have a total of 11", self.card_game.cards_total(cards))    

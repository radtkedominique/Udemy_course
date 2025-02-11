from deck_of_cards import Card
from deck_of_cards import Deck

import unittest

class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.card = Card('2', 'Diamonds')
        self.deck = Deck()

    def test_card__init__(self):
        self.assertEqual(self.card.suit, 'Diamonds')
        self.assertEqual(self.card.value, '2')

    def test_card__repr__(self):
        self.assertEqual(self.card.__repr__(), '2 of Diamonds')

    def test_deck__init__(self):
        self.assertIsInstance(self.deck.cards, list)
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck__repr__(self):
        self.assertEqual(self.deck.__repr__(), 'Deck of 52 cards')

    def test_deck_count(self):
        self.assertEqual(len(self.deck.cards), 52)
        self.deck.cards.pop()
        self.assertEqual(len(self.deck.cards), 51)

    def test_deck__deal_insufficient(self):
        cards = self.deck._deal(60)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test__deal_sufficient(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test__deal_empty(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1) #????

    def test_deal_card(self):
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        hand = self.deck.deal_hand(6)
        self.assertEqual(len(hand), 6)
        self.assertEqual(self.deck.count(), 46)

    def test_shuffle_full_deck(self):
        new_deck = Deck()
        self.deck.shuffle()
        self.assertNotEqual(self.deck, new_deck)
        self.assertEqual(len(self.deck.cards), 52)

    def test_shuffle_empty_deck(self):
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()












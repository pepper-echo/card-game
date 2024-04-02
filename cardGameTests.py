import unittest
from cardGame import Card, Deck, is_group
from random import shuffle, seed


class TestCard(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize cards w/ number/color/shading/shaper"""
        c1 = Card(2, "green", "striped", "diamond")

        self.assertEqual(c1.number, 2)
        self.assertEqual(c1.color, "green")
        self.assertEqual(c1.shading, "striped")
        self.assertEqual(c1.shape, "diamond")

    def test_str(self):
        """test that we can get a good string representation of GroupCard instances"""
        c1 = Card(2, "green", "striped", "diamond")
        self.assertEqual(str(c1), "Card(2, green, striped, diamond)")

    def test_eq(self):
        """Tests that two cards are equal iff all attributes (number, color, shading, shape) are equal"""
        c1 = Card(2, "green", "striped", "diamond")
        c2 = Card(1, "blue", "empty", "oval")
        self.assertTrue(Card.__eq__(c1, c1))
        self.assertFalse(Card.__eq__(c1, c2)) 
        

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.d1 = Deck()         
        self.d2 = Deck()         

    def test_init(self): 
        """Tests that there exists one copy of each possible card within the deck"""
        self.assertEqual((len(self.d1.deck)), 81)

    def test_draw_top(self): 
        """Tests that the player draws a card from the top of the deck (should be last in the list)"""
        seed(657)
        self.assertEqual((shuffle(self.d1.deck)), (shuffle(self.d2.deck)))  

    def test_shuffle(self): 
        """Tests that the deck is shuffled"""
        self.d2.deck.pop()
        self.assertEqual((self.d1.deck[ : -1]), (self.d2.deck)) 


class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.c1 = Card(1, "green", "solid", "squiggle")    
        self.c2 = Card(1, "green", "solid", "squiggle")    
        self.c3 = Card(1, "green", "solid", "squiggle")    
        self.c4 = Card(3, "blue","solid", "squiggle")       
        self.c5 = Card(2,"purple", "empty", "oval")      
        self.c6 = Card(1, "green", "striped", "diamond") 

    def test_is_group(self): 
        """Tests if a group of cards is considered a 'GROUP!'(Either all 3 cards share the same 4 attributes or have 4 completely unique attributes"""
        self.assertTrue(Deck.is_group(self.c1, self.c2, self.c3))  
        
        self.assertTrue(Deck.is_group(self.c4, self.c5, self.c6)) 
        
        self.assertFalse(Deck.is_group(self.c1, self.c5, self.c2)) 



unittest.main() # runs all unittests above


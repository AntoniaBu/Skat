# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:27:30 2022

@author: Toni
"""

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
               
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
               
    def get_name(self):
        return self.get_suit() + ' ' + self.get_rank()
    
    def __repr__(self):
        # how to print a card
        return self.get_name()

class Deck:
    def __init__(self):
        self.cards_in_deck = []
        self.dealt_cards = []
        ranks = ['Ass', '10', 'König', 'Dame', 'Bube', '9', '8', '7']
        suits = ['Kreuz', 'Pik', 'Herz', 'Karo']
        
        for suit in suits:
            for rank in ranks:
                self.cards_in_deck.append(Card(rank, suit))
    
    
    def get_size(self):
        return len(self.cards_in_deck)
    
    def deal_card(self):
        self.dealt_cards.append(self.cards_in_deck.pop())
    
    def shuffle(self):
        return random.shuffle(self.cards_in_deck)



d = Deck()
d.shuffle()

for i in range(10):
    d.deal_card()
print(d.dealt_cards)






class Player:
    pass




class Game:
    pass
    



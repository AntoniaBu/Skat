# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:27:30 2022

@author: Toni
"""

# this clears console and removes all variables
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass


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
        # how name of the card should be shown
        return self.get_suit() + ' ' + self.get_rank()
    
    def __repr__(self):
        # how to print a cards name
        return self.get_name()

class Deck:
    
    cards_in_deck = []
    dealt_cards = []
    
    def __init__(self):
        ranks = ['Ass', '10', 'König', 'Dame', 'Bube', '9', '8', '7']
        suits = ['Kreuz', 'Pik', 'Herz', 'Karo']
        
        for suit in suits:
            for rank in ranks:
                # create full 32 cards deck
                self.cards_in_deck.append(Card(rank, suit))
      
        
    def get_size(self):
        return len(self.cards_in_deck)
    
   
    def deal_cards(self, num):
        # deals as many cards as specified by 'num'
        if self.dealt_cards:
            self.dealt_cards = []
        for i in range(num):
            self.dealt_cards.append(self.cards_in_deck.pop())
        return self.dealt_cards
    
    
    def shuffle(self):
        # shuffles cards in the deck
        return random.shuffle(self.cards_in_deck)


class Player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []
                
    def take_cards(self, hand_cards):
        self.hand.extend(hand_cards)
        
       

class Game:   
        
    def __init__(self):
        pass
    
    def create_players(self, x, y, z):
        p1 = Player(x)
        p2 = Player(y)
        p3 = Player(z)
        return(p1, p2, p3)
    


       
if __name__ == "__main__":
    
  
# =============================================================================
#     x = input("Name player 1: ")
#     y = input("Name player 2: ")
#     z = input("Name player 3: ")
# =============================================================================
    
    x = 'x'
    y = 'y'
    z = 'z'

    g = Game()
    player1, player2, player3 = g.create_players(x, y, z)
    
    d = Deck()
    d.shuffle()
    
    player1.take_cards(d.deal_cards(8))
    print(d.get_size())
    print(player1.hand)
    
    player2.take_cards(d.deal_cards(3))
    print(d.get_size())
    print(player2.hand)
    
    player3.take_cards(d.deal_cards(4))
    print(d.get_size())
    print(player3.hand)
    
    
# =============================================================================
#     print(player1.hand)
#     print(len(player1.hand)) 
#     print(player2.hand)
#     print(len(player2.hand))
#     print(player3.hand)
#     print(len(player3.hand))
# =============================================================================

   
    #print(d.deal_cards(10))
    


# =============================================================================
# class Reizen:
#     # calculates points during reizen
#     def __init__(self, suit, num_B):
#         self.suit = suit
# 
#     def calc_value(self):
#         pass
# =============================================================================


        

    
    
    
    
    
    



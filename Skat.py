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
      
    # how name of the card should be shown         
    def get_name(self):
        return self.get_suit() + ' ' + self.get_rank()
    
    # how to print a cards name
    def __repr__(self):
        return self.get_name()
    
    # define int value for the cards to make them sortable
    def num_rank(self, rank):
        if rank == "Bube":
            return 14
        if rank == "Ass":
            return 13
        if rank == "10":
            return 12
        if rank == "König":
            return 11
        if rank == "Dame":
            return 10
        return int(rank)
    
    def num_suit(self, suit):
        if suit == "Karo":
            return 1
        if suit == "Herz":
            return 2
        if suit == "Pik":
            return 3
        if suit == "Kreuz":
            return 4
        return int(suit)
    
    def __lt__(self, o):     # tuple ordering
        c1 = self.num_suit(self.suit), self.num_rank(self.rank)
        c2 = o.num_suit(o.suit), o.num_rank(o.rank)   
        return c1 < c2

    def __eq__(self, o):
        c1 = self.num_suit(self.suit), self.num_rank(self.rank)
        c2 = o.num_suit(o.suit), o.num_rank(o.rank)
        return c1 == c2
    

class Deck:
    
    cards_in_deck = []
    dealt_cards = []
    
    def __init__(self):
        ranks = ['Ass', '10', 'König', 'Dame', 'Bube', '9', '8', '7']
        suits = ['Kreuz', 'Pik', 'Herz', 'Karo']
        
        # create full 32 cards deck
        self.cards_in_deck = [Card(r,s) for r in ranks for s in suits]
          
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
    
    def order(self):
        self.cards_in_deck.sort()


class Player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []
                
    def take_cards(self, hand_cards):
        self.hand.extend(hand_cards)
      
    def sort_cards(self):
        return self.hand.sort()
        
    def play_card(self):
        pass
        
       

class Game:   
        
    def __init__(self):
        pass
    
    def create_players(self, x, y, z):
        p1 = Player(x)
        p2 = Player(y)
        p3 = Player(z)
        return(p1, p2, p3)
    

class Console:
    
    def init(self):
        pass
    
    def type_player_names(self):
        x = input("Name player 1: ")
        y = input("Name player 2: ")
        z = input("Name player 3: ")
        return(x, y, z)
    
    def select_card(self, hand_cards):
        card = input("\nType the card you want to play: ")
        
# =============================================================================
#         while True:
#             try:
#                 card in hand_cards
#                 break
#             except ValueError:
#                 print('Please select a hand card.')
#                 
#         print('\n' + card + ' was played.')     
# =============================================================================
        return card

       
if __name__ == "__main__":
    
    
    x = 'x'
    y = 'y'
    z = 'z'

    c = Console()
    #x, y, z = c.get_player_names()
    
    # create game
    g = Game()
    # create players
    player1, player2, player3 = g.create_players(x, y, z)
    # create deck
    d = Deck()
    # shuffle deck
    d.shuffle()
    
# =============================================================================
#     d.cards_in_deck.sort()
#     print(d.cards_in_deck)
# =============================================================================

    #players take 10 cards each
    player1.take_cards(d.deal_cards(10))
    player2.take_cards(d.deal_cards(10))
    player3.take_cards(d.deal_cards(10))
    
    #players sort their cards
    player1.sort_cards()
    player2.sort_cards()
    player3.sort_cards()
    
    print('\nPlayer 1 cards: ')
    print(player1.hand)
    
    # player selects a card from their hand they want to play
    # card is removed from their hand
    card_played = c.select_card(player1.hand)
    
    #player1.hand.remove(card_played)

    print('\nPlayer 1 cards: ')
    print(player1.hand)



# =============================================================================
# class Reizen:
#     # calculates points during reizen
#     def __init__(self, suit, num_B):
#         self.suit = suit
# 
#     def calc_value(self):
#         pass
# =============================================================================


        

    
    
    
    
    
    



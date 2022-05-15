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
    
    # define points of a rank
    def num_points(self, rank):
        if rank == "Ass":
            return 11
        if rank == "10":
            return 10
        if rank == "König":
            return 4
        if rank == "Dame":
            return 3
        if rank == "Bube":
            return 2
        if rank == "9" or rank == "8" or rank == "7":
            return 0
        return int(rank)
    
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
    
    # cards are gonna be sorted by suit & rank
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
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.hand = []
                
    def take_cards(self, hand_cards):
        self.hand.extend(hand_cards)
      
    def sort_cards(self):
        return self.hand.sort()
        
    def play_card(self, current_player, console):
        print('\nPlayer ' + current_player.number + ' cards: ')
        print(current_player.hand)
        
        # player selects a card from their hand they want to play
        card_played = console.select_card(current_player.hand)
        
        # new Card object is instantiated
        card_played = Card(card_played[1], card_played[0])
        
        # card is removed from their hand
        current_player.hand.remove(card_played)
    
        print('\nPlayer ' + current_player.number + ' cards: ')
        print(current_player.hand)
        
        input("\nPress Enter to continue...")
        
        return card_played
       

class Game:   
        
    def __init__(self):
        pass
    
    def create_players(self, x, y, z):
        p1 = Player(x, '1')
        p2 = Player(y, '2')
        p3 = Player(z, '3')
        return(p1, p2, p3)
    
    def players_take_cards(self):
        pass
    
    def players_sort_cards(self):
        pass
    

    

 
# =============================================================================
# class GamePoints:
#     
#     points = 0
#     
#     def __init__(self):
#         pass
#  
#     def count_stitch(self, c1, c2, c3):
#         card1 = Card(c1[1], c1[0])
#         card2 = Card(c2[1], c2[0])
#         card3 = Card(c3[1], c3[0])
#         
#         #return card1.num_points(c1) + card2.num_points(c2) + card3.num_points(c3)
#         pass
# =============================================================================
    
    
class Console:
    
    def init(self):
        pass
    
    def get_player_names(self):
        x = input("Name player 1: ")
        y = input("Name player 2: ")
        z = input("Name player 3: ")
        return(x, y, z)
    
    def select_card(self, hand_cards):
        ###### TO DO !!!!!
        # check if input has the correct form and can be handled by Card class
        card_played = input("\n1 Type the card you want to play: \n").strip()
        # card string is splitted
        card = card_played.split(' ')
        
# =============================================================================
#         while not(len(card) == 2):
#             print('\n2 Please select a hand card.')
#             card_played = input("\n2 Type the card you want to play: \n").strip()   
#             card = card_played.split(' ')
#         # new Card object is instantiated
#         card = Card(card[1], card[0])
#         
#         while True:
#             try:
#                 card_played = input("\n3 Type the card you want to play: \n").strip()  
#                 card = card_played.split(' ')
#                 # new Card object is instantiated
#                 card = Card(card[1], card[0])
#                 card = card in hand_cards
#                 break
#             except ValueError:
#                 print('\n3 Please select a hand card.')
#         print('YEY')
# =============================================================================
                
            
        while not(len(card) == 2):
            print('\n2 Please select a hand card.')
            card_played = input("\n2 Type the card you want to play: \n").strip()   
            card = card_played.split(' ')
            # new Card object is instantiated
            card = Card(card[1], card[0])
            
# =============================================================================
#         while True:
#             try:                    
#                 card = card in hand_cards
#                 break
#             except ValueError:
#                 print('\n3 Please select a hand card.')
#         print('YEY')
#                 
# =============================================================================

              
               
          
            
        print('\n' + card_played + ' was played.')     
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
    
    
    #players take 10 cards each
    player1.take_cards(d.deal_cards(10))
    player2.take_cards(d.deal_cards(10))
    player3.take_cards(d.deal_cards(10))
    
    #players sort their cards
    player1.sort_cards()
    player2.sort_cards()
    player3.sort_cards()


    stitches = 0
      
    while (player1.hand):
    # while players still hold cards in their hands
    
        # player 1 is playing a card
        c1 = player1.play_card(player1, c)       
        points_c1 = c1.num_points(c1.rank)
    
        # player 2 is playing a card
        c2 = player2.play_card(player2, c)
        points_c2 = c2.num_points(c2.rank)
        
        # player 3 is playing card
        c3 = player3.play_card(player3, c)
        points_c3 = c3.num_points(c3.rank)
        
        
        # count stitch points
        stitch = points_c1 + points_c2 + points_c3
        print('\n---Current stitch points: ' + str(stitch) + '---')

        stitches += stitch
        
        print('\n---All stitch points together: ' + str(stitches) + '---')


# =============================================================================
# class Reizen:
#     # calculates points during reizen
#     def __init__(self, suit, num_B):
#         self.suit = suit
# 
#     def calc_value(self):
#         pass
# =============================================================================


        

    
    
    
    
    
    



"""
This is a coding exercise.
It aims to show the use of:
    - Functions
    - Typing Hints

The goal is:
    - Create a deck of cards
    - Shuffle it
    - Split it to a N number of players
    - Each player receive the same amount of cards

This exercise is part of the online course:
https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/
"""

import random
from typing import List,Tuple

# Number of players in the game
number_of_players = 3

# from https://www.alt-codes.net/suit-cards.php
suits = '♠ ♡ ♢ ♣'.split()
cards = '2 3 4 5 6 7 8 9 10 J Q K A'.split() 

card = Tuple[str,str]
deck = List[card]

def set_deck(shuffle: bool = False) -> deck:
    """ This creates a deck with 52 cards
        This deck is a list of tuples, and each tuple is a card"""
    deck  = [(n,c) for c in cards for n in suits]
    if shuffle:
        random.shuffle(deck)
    return deck

def deliver_cards(deck: deck, number_of_players: int) -> List:
    """Deliver the cards to each player"""
    number_of_cards = 52 // number_of_players
    hands: List = [[] for i in range(number_of_players)]
    n=0
    for i in range(number_of_cards):
        for j in range(number_of_players):
            hands[j].append(deck[n])
            n+=1
    return hands

def names(number_of_players: int) -> List[str]:
    """Name the players as P1, P2, P3 and so on"""
    name = []
    for i in range(number_of_players):
        name.append(f'P{i+1}')
    return name

"""Create a new deck"""
new_deck = set_deck(shuffle=True)

"""Create names for each player"""
players = names(number_of_players)

"""Create a hand for each player"""
hands = {j: m for j, m in zip(players,deliver_cards(new_deck,number_of_players))}

"""Show the hand of each player"""
for player, new_deck in hands.items():
    new_cards = ' '.join(f"{j}{c}" for (j,c) in new_deck)
    print(f'{player}: {new_cards}')

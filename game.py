"""
This is a coding exercise.
It aims to show the use of:
    - Functions
    - Typing Hints

The goal is:
    - Create a deck of cards
    - Shuffle it
    - Split it to a N number of players

This exercises is part of the online course:
https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/
"""

import random
from typing import List,Tuple

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

def deliver_cards(deck: deck) -> Tuple:
    """Deliver the cards to each player"""
    return (deck[0::4],deck[1::4],deck[2::4],deck[3::4])

"""Inicia um jogo de cards para 4 jogadores"""
new_deck = set_deck(shuffle=True)
players = 'P1 P2 P3 P4'.split()
hands = {j: m for j, m in zip(players,deliver_cards(new_deck))}
    
for player, new_deck in hands.items():
    new_cards = ' '.join(f"{j}{c}" for (j,c) in new_deck)
    print(f'{player}: {new_cards}')

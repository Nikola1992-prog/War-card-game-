import random

# Card suits and Ranks
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Card values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# three_of_clubs = Card('Clubs', 'Three')
# two_harts = Card('Harts', "Two")
# print(three_of_clubs.value > two_harts.value)

class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()

# new_dack = Deck()
# for card in new_dack.all_cards:
#     print(card)

class Player():

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        if type(new_cards) == type([]):
            # List od multiple Card obj
            self.all_cards.extend(new_cards)
        else:
            # For a single card obj
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# new_player = Player('Nikola')
# print(new_player)
#
# two_harts = Card('Harts', "Two")
# three_of_clubs = Card('Clubs', 'Three')
#
# new_player.add_cards(two_harts)
# new_player.add_cards(three_of_clubs)
# new_player.add_cards([three_of_clubs,three_of_clubs,three_of_clubs])
#
# for card in new_player.all_cards:
#     print(card)
#
# print(new_player)
# print(new_player.remove_one())
# print(new_player)

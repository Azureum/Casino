import random
import time

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        suit_symbols = {
            'hearts': '♥',
            'diamonds': '♦',
            'clubs': '♣',
            'spades': '♠'
        }
        return f"{self.rank}{suit_symbols[self.suit]}"
    
    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def calculate_value(self):
        value = sum(card.value() for card in self.cards)
        aces = sum(card.rank == 'A' for card in self.cards)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards) + f" (Value: {self.calculate_value()})"

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deal_initial_cards()
    
    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())
    
    def player_hit(self):
        self.player_hand.add_card(self.deck.draw_card())
    
    def dealer_play(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.draw_card())
    
    def check_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        
        if player_value > 21:
            return "Player busts! Dealer wins."
        elif dealer_value > 21:
            return "Dealer busts! Player wins."
        elif player_value > dealer_value:
            return "Player wins!"
        elif dealer_value > player_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"
    
    def play(self):
        print("Dealer's hand:", self.dealer_hand.cards[0])
        print("Player's hand:", self.player_hand)
        
        while self.player_hand.calculate_value() < 21:
            action = input("Do you want to hit or stand? (h/s): ")
            if action.lower() == 'h':
                self.player_hit()
                print("Player's hand:", self.player_hand)
            else:
                break
        
        if self.player_hand.calculate_value() <= 21:
            self.dealer_play()
            print("Dealer's hand:", self.dealer_hand)
        
        print(self.check_winner())

print("Welcome to the Casino!")
print("Choose a game:")
print("1: Blackjack")

choice = input("Enter a number: ")

if choice == "1":
    BlackjackGame().play()
else:
    print("Exiting the Casino.")
    time.sleep(2)
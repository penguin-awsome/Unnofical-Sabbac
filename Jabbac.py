#Imports:
import time #'cause I like pauses for no good reason
import random #for things like dice rolls, shuffling, and card draws

#variables
credits = 0


#Classes:
class Card:
    def __init__(self, card, polarity, value, stave):
        self.card = card
        self.type = polarity
        self.value = value
        self.stave = stave

    def __repr__(self):
        return f"{self.card}"
  
class Deck:
    def __init__(self):
        self.cards = [
            #list of cards
                #Cylops
            Card("Cylop", "neutral", 0, None),
            Card("Cylop", "neutral", 0, None),
                #Positive
                    #Triangles
            Card("Tri-Pos-1", "positive", 1, "triangles"),
            Card("Tri-Pos-2", "positive", 2, "triangles"),
            Card("Tri-Pos-3", "positive", 3, "triangles"),
            Card("Tri-Pos-4", "positive", 4, "triangles"),
            Card("Tri-Pos-5", "positive", 5, "triangles"),
            Card("Tri-Pos-6", "positive", 6, "triangles"),
            Card("Tri-Pos-7", "positive", 7, "triangles"),
            Card("Tri-Pos-8", "positive", 8, "triangles"),
            Card("Tri-Pos-9", "positive", 9, "triangles"),
            Card("Tri-Pos-10", "positive", 10, "triangles"),
                    #squares
            Card("Sqr-Pos-1", "positive", 1, "squares"),
            Card("Sqr-Pos-2", "positive", 2, "squares"),
            Card("Sqr-Pos-3", "positive", 3, "squares"),
            Card("Sqr-Pos-4", "positive", 4, "squares"),
            Card("Sqr-Pos-5", "positive", 5, "squares"),
            Card("Sqr-Pos-6", "positive", 6, "squares"),
            Card("Sqr-Pos-7", "positive", 7, "squares"),
            Card("Sqr-Pos-8", "positive", 8, "squares"),
            Card("Sqr-Pos-9", "positive", 9, "squares"),
            Card("Sqr-Pos-10", "positive", 10, "squares"),
                    #Circles
            Card("Cir-Pos-1", "positive", 1, "circles"),
            Card("Cir-Pos-2", "positive", 2, "circles"),
            Card("Cir-Pos-3", "positive", 3, "circles"),
            Card("Cir-Pos-4", "positive", 4, "circles"),
            Card("Cir-Pos-5", "positive", 5, "circles"),
            Card("Cir-Pos-6", "positive", 6, "circles"),
            Card("Cir-Pos-7", "positive", 7, "circles"),
            Card("Cir-Pos-8", "positive", 8, "circles"),
            Card("Cir-Pos-9", "positive", 9, "circles"),
            Card("Cir-Pos-10", "positive", 10, "circles"),
                #Negative
                    #Triangles
            Card("Tri-Neg-1", "negative", 1, "triangles"),
            Card("Tri-Neg-2", "negative", 2, "triangles"),
            Card("Tri-Neg-3", "negative", 3, "triangles"),
            Card("Tri-Neg-4", "negative", 4, "triangles"),
            Card("Tri-Neg-5", "negative", 5, "triangles"),
            Card("Tri-Neg-6", "negative", 6, "triangles"),
            Card("Tri-Neg-7", "negative", 7, "triangles"),
            Card("Tri-Neg-8", "negative", 8, "triangles"),
            Card("Tri-Neg-9", "negative", 9, "triangles"),
            Card("Tri-Neg-10", "negative", 10, "triangles"),
                    #squares
            Card("Sqr-Neg-1", "negative", 1, "squares"),
            Card("Sqr-Neg-2", "negative", 2, "squares"),
            Card("Sqr-Neg-3", "negative", 3, "squares"),
            Card("Sqr-Neg-4", "negative", 4, "squares"),
            Card("Sqr-Neg-5", "negative", 5, "squares"),
            Card("Sqr-Neg-6", "negative", 6, "squares"),
            Card("Sqr-Neg-7", "negative", 7, "squares"),
            Card("Sqr-Neg-8", "negative", 8, "squares"),
            Card("Sqr-Neg-9", "negative", 9, "squares"),
            Card("Sqr-Neg-10", "negative", 10, "squares"),
                    #Circles
            Card("Cir-Neg-1", "negative", 1, "circles"),
            Card("Cir-Neg-2", "negative", 2, "circles"),
            Card("Cir-Neg-3", "negative", 3, "circles"),
            Card("Cir-Neg-4", "negative", 4, "circles"),
            Card("Cir-Neg-5", "negative", 5, "circles"),
            Card("Cir-Neg-6", "negative", 6, "circles"),
            Card("Cir-Neg-7", "negative", 7, "circles"),
            Card("Cir-Neg-8", "negative", 8, "circles"),
            Card("Cir-Neg-9", "negative", 9, "circles"),
            Card("Cir-Neg-10", "negative", 10, "circles"),
            
        ]

    def __repr__(self):
        return "\n".join([repr(card) for card in self.cards])

    def shuffle(self):
        random.shuffle(self.cards) 
        return self.cards
    
    def draw(self):
        return self.cards.pop() 
    
class Player:
    def __init__(self, name, credits):
        self.name = name
        self.hand = []
        self.credits = credits
        self.scrapped = False
        self.ingame = True

class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.pot = 0
        self.hand = 0

    def ante(self):
        for player in self.players:
            if player.ingame and player.credits > 0:
                player.credits -= 1
                self.pot += 1
    
    def deal(self):
        cards_to_deal = 2
        for player in self.players:
            for _ in range(cards_to_deal):
                if self.deck.cards:
                    card = self.deck.draw()
                    player.hand.append(card)
        return [(player.name, player.hand) for player in self.players]
    
    def player_actions(self):
        pass

    def betting_phase(self):
        pass

    def dice_roll(self):
        dice1 = 0
        dice2 = 0
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == dice2:
            print("re-draw hands:", dice1, dice2)
        else:
            print("safe:", dice1, dice2)

    def reveal_hands(self):
        pass

    def game_loop(self):
        self.deck.shuffle()
        self.ante()
        self.deal()
        for rounds in range(3):
            self.player_actions()
            self.betting_phase()
            random_dice = self.dice_roll()
        self.reveal_hands()

deck = Deck()
shuffled_deck = deck.shuffle()
#print(shuffled_deck)
Penguin = Player("Penguin", 3)
game = Game([Penguin])
game.dice_roll()
dealt_player_hands = game.deal()
print(dealt_player_hands)
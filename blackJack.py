import random

suits =('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks

    def __str__(self):
        return self.ranks+ " of "+ self.suits
class deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has:"+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class hand:
    def __init__(self):

        self.card=[]
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.card.append(card)
        self.value= self.value +  values[card.ranks]

        if card.ranks == 'Ace':
            self.aces+=1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class chips:
    def __init__(self,total=100):
        self.total = total
        self.bet=0

    def win_bet(self):
        self.total += self.bet

    def loss_bet(self):
        self.total -= self.bet

#function definitions
def take_bet(chips):
    while True:
        try:
            chips.bet= int(input("How many chips you want to bet?"))
        except:
            print("Sorry pls provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have enough chips! you have {}".format(chips.total))
            else:
                break
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or stand?Enter h or s")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("PLayer stands dealer's turn")
            playing =  False
        else:
            print("sorry i didn't understand that. pls enter s and h only")
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.card[1])
    print("\nPlayer's Hand:", *player.card, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.card, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.card, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(player,dealer,chips):
    print("Bust player!")
    chips.loss_bet()

def player_wins(player,dealer,chips):
    print("player wins")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("player wins !dealer busts")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("dealer wins")
    chips.loss_bet()

def push(player,dealer):
    print("Dealer and player tie!! PUSH")

#gameplay!
while True:
    print("Welcome to blackjack!")

    Deck= deck()
    Deck.shuffle()

    player_hand = hand()
    player_hand.add_card(Deck.deal())
    player_hand.add_card(Deck.deal())

    dealer_hand = hand()
    dealer_hand.add_card(Deck.deal())
    dealer_hand.add_card(Deck.deal())

    player_chips = chips()

    take_bet(player_chips)
    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(Deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(Deck,dealer_hand)

        show_all(player_hand,dealer_hand)


        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print("\n player total chips are at : {}".format(player_chips.total))

    new_game = input("like to play again? y/n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank u for playing!")

        break





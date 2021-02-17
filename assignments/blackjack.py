import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f'{self.value} of {self.suit}')

class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        for c in suits:
            for v in values:
                self.cards.append(Card(c, v))
    
    def shuffle(self):
        print('shuffling cards\n')
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, len(self.cards)-1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw(self):
        return self.cards.pop()

    def clear(self):
        self.cards = []

class Player:
    def __init__(self, name, bet, total=0, hand=[], is_busted=False):
        self.name = name
        self.bet = bet
        self.total = total
        self.hand = hand
        self.is_busted = is_busted

    def show(self):
        print("{}'s HAND:".format(self.name))
        for card in self.hand:
            card.show()
        print('TOTAL: {}'.format(self.total))

    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)
        return card

    def clear(self):
        self.hand = []
        self.total = 0

class Blackjack:
    def __init__(self, deck):
        self.deck = deck
        self.active_player = 'player'
        self.users = []
    
    def start(self, player):
        self.users.append(player)

    def new_game(self):
        self.deck = deck
        deck.clear()
        deck.build()
        deck.shuffle()
        if self.users is not []:
            for player in self.users:
                player.hand = []
                player.total = 0
                #player.draw(deck)
                #player.draw(deck)
                #player.show()
        

    def show(self):
        for user in self.users:
            user.show()
    
    def player_ace(self):
        for card in self.active_player.hand:
            if card.value == 'Ace':
                ace_choice = input(card.value, ' of ', card.suit, ' 1 or 11?\n')
                if ace_choice == 1:
                    self.active_player.total += 1
                elif ace_choice == 11:
                    self.active_player.total += 11
                else:
                    ValueError

    def dealer_ace(self):
        if self.active_player.total + 11 > 21:
            self.active_player.total += 1
        else:
            self.active_player.total +=11

    def hit(self, deck):
        card = self.active_player.draw(deck)
        if card.value == "Ace":
            if self.active_player.name == "dealer":
                self.dealer_ace()
        elif card.value == "Jack" or card.value == "Queen" or card.value == "King":
            self.active_player.total += 10
        else:
            self.active_player.total += card.value
        self.active_player.show()
    
    def stand(self):
        self.player_ace()
        self.active_player.show()

    def bust_check(self):
        if self.users[0].total > 21:
            self.users[0].is_busted = True
            print(self.users[0].name, ' busted!')

    def dealerTurn(self, deck):       
        while self.active_player == dealer:
            player = self.active_player
            if self.users[0].is_busted == True:
                print(self.users[0].name, 'busted, dealer wins')
                break
            elif player.total < 17:
                self.hit(deck)
                player.show()
                continue
            elif player.total > 21:
                print('DEALER BUSTS, YOU WIN!!!')
                break
            else:
                print('DEALER STANDS!\n')
                break
            player.show()

    def determine_winner(self):
        if self.users[0].total > self.users[1].total and self.users[0].total <= 21:
            print(self.users[0].name, ' wins!!!')
        elif self.users[0].total <= 21 and self.users[1].total > 21:
            print(self.users[0].name, ' wins!!!')
        else:
            print('Dealer wins!!! D:')

    def set_active_player(self, deck):
        for player in self.users:
            self.active_player = player
            player.hand = []
            while True:
                if self.active_player.name == "dealer":
                    self.dealerTurn(deck)
                    break
                else:   
                    turn = input('hit or stand?\n')
                    if turn.lower() == 'hit':
                        self.hit(deck)
                        self.bust_check()
                        if player.is_busted == True:
                            break
                    elif turn.lower() == 'stand':
                        self.stand()
                        break
            self.show()
        self.determine_winner()

    
                         
                        

while True:
    deck = Deck()
    deck.build()
    joshua = Player("josh", 0)
    dealer = Player("dealer", 0)
    game = Blackjack(deck)
    blackjack = input('Ready to play Blackjack? (Y/N)\n')
    if blackjack.lower() == 'y':
        game.start(joshua)
        game.start(dealer)
        game.new_game()
        game.set_active_player(deck)
        
        
    else:
        break






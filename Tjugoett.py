import time
from random import shuffle


class CardGames:
    def __init__(self, player_name="Player", dealer_name="Dealer"):
        self.kort: dict = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10, "ace": 14,
            "queen": 12, "jack": 11, "king": 13
        }
        self.lista_kort = list(self.kort.keys())
        self.player_name: str = player_name
        self.dealer_name: str = dealer_name
        self.cardlist: list = self.lista_kort[:]
        self.player: list = []
        self.dealer: list = []

    def shuffle_card(self):
        shuffle(self.cardlist)

    def player_calculate_value(self, hand):
        player_points = 0
        aces = 0

        for card in hand:
            if card == "ace":
                aces += 1
                player_points += 14  # Räkna esset som 14 till att börja med
            else:
                player_points += self.kort[card]

        # Justera poäng för ess om poängen överstiger 21
        while player_points > 21 and aces:
            player_points -= 13  # Minska poängen från 14 till 1
            aces -= 1

        return player_points

    def dealer_calculate_value(self, hand):
        dealer_points = 0
        aces = 0

        for card in hand:
            if card == "ace":
                aces += 1
                dealer_points += 14
            else:
                dealer_points += self.kort[card]

        while dealer_points > 21 and aces:
            dealer_points -= 13
            aces -= 1

        return dealer_points

    def dealing_the_cards(self):
        print("Hello and Welcome to tjugoettan! You will receive two cards and the dealer will show you the first card.")
        
        # Dra två kort för spelaren
        for _ in range(2):
            players_cards = self.cardlist.pop()
            if players_cards == "ace":
                choose_ace = input("You got an ace, would you like 1 or 14? (1/14): ")
                if choose_ace == "1":
                    self.player.append("ace")  # Räkna esset som 1
                else:
                    self.player.append("ace")  # Räkna esset som 14
            else:
                self.player.append(players_cards)

            time.sleep(1)

        print(f'You get {self.player[-1]}')  # Skriv ut det senaste kortet som drogs
        dealers_card = self.cardlist.pop()
        self.dealer.append(dealers_card)
        print(f'The dealer gets {dealers_card}')
        time.sleep(1)

    def player_continue(self):
        while self.player_calculate_value(self.player) <= 21:
            print(f'You have {self.player}, do you wish to draw more? Y/N')
            draw_more_cards = input()
            if draw_more_cards.upper() == "Y":
                players_cards = self.cardlist.pop()
                self.player.append(players_cards)
                print(f'You got {players_cards}')
            elif draw_more_cards.upper() == "N":
                print("You choose to stay at your current points. The dealer will commence drawing cards.")
                break

    def dealer_continue(self):
        while self.dealer_calculate_value(self.dealer) < 17:  # Dealer drar kort tills de når 17 eller mer
            dealers_card = self.cardlist.pop()
            self.dealer.append(dealers_card)
            print(f'The dealer has drawn {dealers_card}')
            time.sleep(1)

    def blackjack(self):
        if self.player_calculate_value(self.player) == 21:
            print("Black Jack, you win!")
        if self.dealer_calculate_value(self.dealer) == 21:
            print("The dealer has Black Jack!")

    def winner(self, dealer_points, player_points):
        if player_points > 21:
            print("You lose! You went over 21.")
        elif dealer_points > 21:
            print("You win! The dealer went over 21.")
        elif player_points > dealer_points:
            print("You win!")
        elif player_points == dealer_points:
            print("It's a draw")
        else:
            print("You lose!")

def start_game():
    while True:
        game = CardGames()
        game.shuffle_card()
        game.dealing_the_cards()

        player_points = game.player_calculate_value(game.player)
        dealer_points = game.dealer_calculate_value(game.dealer)

        game.player_continue()
        game.dealer_continue()
        game.blackjack()

        # Beräkna poäng igen efter att spelaren och dealern har dragit kort
        player_points = game.player_calculate_value(game.player)
        dealer_points = game.dealer_calculate_value(game.dealer)

        game.winner(dealer_points, player_points)

        play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
        if play_again != "ja":
            print("Tack för att du spelade! Hej då!")
            break
        else:
            print("\n--- Nytt spel börjar ---\n")

if __name__ == "__main__":
    start_game()

#!/usr/bin/env python3

import random
import cards

def show_cards(hand, flag):
    if flag == True:
        card = hand[0]
        print(card[2] + " of " + card[1])
    else:
        for card in hand:
            print(card[2] + " of " + card[1])

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def play_hand(dealer_score, player_score):
    if player_score > 21:
        return "lose"
    elif player_score == 21:
            return "blackjack"
    elif (player_score < 21 and player_score > dealer_score) or (dealer_score > 21):
            return "win"
    elif player_score == dealer_score:
            return "push"
    else:
            return "lose"

dealer_hand = []
player_hand = []

def main():
    display_title()
    money = float(input("Starting money: "))
    while money <= 0:
        print("You must start with more than 0!")
        print()
        money = float(input("Starting money: "))
    print()
    play_again = "y"
    while money > 0 and play_again == "y":
        bet_amount = float(input("Bet amount: "))
        while bet_amount <= 0:
            print("Bet amount must be more than 0!")
            print()
            bet_amount = float(input("Bet amount: "))
        while bet_amount > money:
            print("Sorry, you only have ", money)
            print()
            bet_amount = float(input("Bet amount: "))
        print()
        dealer_hand = []
        player_hand = []
        deck = cards.get_deck()
        random.shuffle(deck)
        dealer_hand.append(cards.get_card(deck))
        dealer_hand.append(cards.get_card(deck))
        player_hand.append(cards.get_card(deck))
        player_hand.append(cards.get_card(deck))
        print("Dealer Hand:")
        show_cards(dealer_hand, True)
        print()
        print("Player Hand:")
        show_cards(player_hand, False)
        print()
        hit_or_stand = input("Hit or stand? (hit/stand): ")
        print()
        while hit_or_stand == "hit":
            player_hand.append(cards.get_card(deck))
            print("Player hand:")
            show_cards(player_hand, False)
            print()
            if cards.get_score(player_hand) > 21:
                print("Sorry, your hand is over 21.")
                print()
                break
            hit_or_stand = input("Hit or stand? (hit/stand): ")
            print()
        while cards.get_score(dealer_hand) < 17:
            dealer_hand.append(cards.get_card(deck))
        print("Dealer's hand:")
        show_cards(dealer_hand, False)
        print()
        dealer_score = cards.get_score(dealer_hand)
        player_score = cards.get_score(player_hand)
        print("YOUR POINTS:      ", player_score)
        print("DEALER'S POINTS:  ", dealer_score)
        print()
        result = play_hand(dealer_score, player_score)
        if result.lower() == "blackjack":
            print("Wow! You got a blackjack!")
            money += bet_amount * 1.5
            money = round(money, 2)
        elif result.lower() == "win":
            print("Hooray! You win!")
            money += bet_amount
        elif result.lower() == "push":
            print("You pushed.")
        elif result.lower() == "lose":
            print("Sorry, you lost.")
            money -= bet_amount
        print("Money: ", money)
        print()
        if money > 0:
            play_again = input("Play again? (y/n): ")
            print()
        
    print("Bye!")

if __name__ == "__main__":
    main()

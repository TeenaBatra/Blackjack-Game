############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
#################################################################

import random
from art import logo
from replit import clear

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []


# deal_card() function that draws a random card and return it
def deal_card():
    cards_drawn = random.choice(cards)
    return cards_drawn


# calculate the score of list of cards and return it
def calculate_score(lst):
    sum = 0
    for i in lst:
        sum += i

        # This checks for a blackjack(ace+10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if sum == 21 and len(lst) == 2:
            return 0

        if sum > 21 and 11 in lst:
            for i in range(0, len(lst) - 1):
                if lst[i] == 11:
                    lst[i] = 1
    return sum


# compare the user's score and dealer's score
def compare(user_score, dealer_score):
    if user_score == dealer_score:
        print("DRAW")
    elif user_score == 0:
        print("you win with a Blackjack.")
    elif dealer_score == 0:
        print("Dealer wins with a Blackjack.")
    elif user_score > 21:
        print("Overflow...you loses!")
    elif dealer_score > 21:
        print("overflow...Dealer loses!")
    elif user_score > dealer_score:
        print(f"You wins with {user_score}")
    else:
        print(f"Dealer wins with {dealer_score}")


game_ended = False
dont_run_again = False

# Deal the user and computer 2 cards each using deal_card() and append().
while not dont_run_again:
    user_cards = []
    dealer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    total_user_cards = calculate_score(user_cards)
    total_dealer_card = calculate_score(dealer_cards)
    print(f"Your cards: {user_cards} and current score is: {total_user_cards}")
    print(f"The first card of dealer is: [{dealer_cards[0]}]")

    while game_ended != True:
        if total_user_cards == 0:
            game_ended = True
            break
        if total_dealer_card == 0:
            game_ended = True
            break

        draw_card = input("Want to draw a card? yes or no:\n").lower()
        if draw_card == "yes":
            user_cards.append(deal_card())
            print(f"My cards are now: {user_cards}")
            total_user_cards = calculate_score(user_cards)
            print(f"The total score is: {total_user_cards}")
            if total_user_cards > 21:
                game_ended = True
                break

        else:
            game_ended = True
            while total_dealer_card != 0 and total_dealer_card <= 16:
                dealer_cards.append(deal_card())
                total_dealer_card = calculate_score(dealer_cards)
            print(f"Dealer's cards now: {dealer_cards}")
            compare(total_user_cards, total_dealer_card)
    if game_ended == True:
        print(f"Your final cards: {user_cards} and total_score: {total_user_cards}")
        print(f"Dealer's final card: {dealer_cards} and total_score: {total_dealer_card}")
        compare(total_user_cards, total_dealer_card)
    run_again = input("Wants to play blackjack game again? Yes or No: ").lower()
    if run_again == "yes":
        clear()
    else:
        dont_run_again = True
        print("HOPE TO SEE YOU AGAIN!")

import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "Dealer wins with Blackjack!"
    elif player_score == 0:
        return "You win with Blackjack!"
    elif player_score > 21:
        return "You went over. Dealer wins!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins!"

def blackjack_game():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        
        print(f"Your hand: {player_hand}, score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            action = input("Type 'hit' to get another card or 'stand' to hold: ").lower()
            if action == "hit":
                player_hand.append(deal_card())
            else:
                game_over = True

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    blackjack_game()
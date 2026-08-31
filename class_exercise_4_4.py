import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def hand_value(hand):
    total = sum(hand)

    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)

    return total


player = [random.choice(cards), random.choice(cards)]
dealer = [random.choice(cards), random.choice(cards)]

print("Welcome to Blackjack!")
print("Your cards:", player, "Total:", hand_value(player))
print("Dealer shows:", dealer[0])

while hand_value(player) < 21:
    choice = input("Hit or stand? ").lower()

    if choice == "hit":
        player.append(random.choice(cards))
        print("Your cards:", player, "Total:", hand_value(player))
    elif choice == "stand":
        break
    else:
        print("Please type hit or stand.")

if hand_value(player) > 21:
    print("Bust! You lose.")
else:
    while hand_value(dealer) < 17:
        dealer.append(random.choice(cards))

    print("\nDealer cards:", dealer, "Total:", hand_value(dealer))
    print("Your total:", hand_value(player))

    if hand_value(dealer) > 21 or hand_value(player) > hand_value(dealer):
        print("You win! 🎉")
    elif hand_value(player) == hand_value(dealer):
        print("It's a draw!")
    else:
        print("Dealer wins!")

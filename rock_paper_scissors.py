# Rock-Paper-Scissors Game

import random 
 
def get_hand(hand):
    # 0 = scissors, 1 = rock, 2 = paper
    hands= ["scissor", "rock", "paper"]
    return hands[hand]

def determine_winner(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "It's a tie!"
    elif (player_hand == "rock" and computer_hand == "scissor") or \
         (player_hand == "scissor" and computer_hand == "paper") or \
         (player_hand == "paper" and computer_hand == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
    
# GAME STARTS HERE
while True:
    try:
        user_input = int(input("Enter a number (0 = scissor, 1 = rock, 2 = paper): "))
        if user_input not in [0, 1, 2]:
            print("Invalid number. Please enter: 0, 1, or 2.")
            continue
    
        computer_input = random.randint(0, 2)

        player_hand = get_hand(user_input)
        computer_hand = get_hand(computer_input)

        print(f"\nYou chose: {player_hand}")
        print(f"Computer chose: {computer_hand}")

        result = determine_winner(player_hand, computer_hand)
        print("Result:", result)
    
        break

    except ValueError:
        print("That wasn't a number. Please enter: 0, 1, or 2.")

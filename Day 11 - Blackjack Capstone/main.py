import art
import random
print(art.logo)

def player_card1():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choices(cards,k=2)

def computer_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choices(cards,k=2)

def additional_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

cards_1 = (player_card1())
computer = computer_card()
print(f"your cards are {cards_1}")
print(f"Computer's 1 Random Card is: {(computer[0])} ") #Computer 1 Random Card Print
score = sum(cards_1)
if 11 in cards_1:
    initial_ace = int(input("Do you want to keep the value of ace as 11 or 1? "))
    if initial_ace == 11:
        score = sum(cards_1)
    else:
        score -= 10
        if cards_1[0] == 11:
            cards_1[0] = 1
        else:
            cards_1[1] = 1


get_another_card = True
while get_another_card: #own card score
        pick_card = input("Do you want to get another card. Y or N ").lower()
        if pick_card == "n":
            get_another_card = False
        else:
            h = additional_card()
            print(f"Your additional card is {h}")
            cards_1.append(h)
            score = sum(cards_1)
            if h == 11:
                ace = int(input("Do you want to keep the value of ace as 11 or 1? "))
                if ace == 11:
                    print(f"Your ace value is {score}")
                else:
                    score -= 10
                    cards_1[-1] = 1
                    print(f"Your ace value is {score}")
            else:
                print(f"your score is {score}")

while sum(computer) < 17:
    v = additional_card()
    computer.append(v)
computer_sum = sum(computer)

print(f"Your final hand: {cards_1}, final score: {score}")
print(f"Computer's final hand: {computer}, final score: {computer_sum}")

if score > 21:
    print("You loose")
elif computer_sum > 21:
    print("Computer Lose")
elif computer_sum == score == 21:
    print("Burst! Tie")
elif computer_sum == score < 21:
    print("Tie")
elif score > computer_sum:
    print("You win")
else:
    print("You loose")


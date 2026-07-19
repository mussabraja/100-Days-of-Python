import random
import art

print(art.logo)

number = random.randint(1,100)
attempts = 0

number_guess = True
difficulty_level = input("Do you want to keep it Easy or Hard ").lower()


def difficulty():
    global attempts
    if difficulty_level == "easy":
        attempts += 10
        print("You have 10 lives")
    else:
        attempts += 5
        print("You have 5 lives")
    return

difficulty()

while number_guess:
    guess_number = int(input("Guess the number "))
    if guess_number == number:
        number_guess = False
        print("Correct Guess")
    else:
        attempts -= 1
        if attempts > 0:
            if guess_number > number:
                print("Too High")
                print(f"You have {attempts} left")
            elif guess_number < number:
                print("Too Low")
                print(f"You have {attempts} left")
        else:
            number_guess = False
            print(f"You loose, correct number was {number}")










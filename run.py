import sys
import random
# modify score varible
user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors Game.")
user_name = input("Please Enter Your Name? ")


def game(user_input):
    """calculate the computer option"""
    random_number = random.randint(0, 2)

    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f'{user_name} picked {user_input} .')
    print(f'Computer picked {computer_pick} .')
    get_result(user_input, computer_pick)


def get_result(user_input, computer_pick):
    """check the result"""
    global user_score, computer_score

    if user_input == computer_pick:
        print("\tMatch has been the same!")
    elif user_input == "rock" and computer_pick == "scissors":
        print("\tYou Won!")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("\tYou Won!")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("\tYou Won!")
        user_score += 1
    else:
        print("\tComputer Won!")
        computer_score += 1
    return user_input, user_score, computer_score


# main section and game start point
while True:
    user_input = input("Type Rock , Paper , Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        continue
    else:
        game(user_input)

# output (when palyer exit the game)
print(f'You won [{user_score}] times.')
print(f'The computer won [{computer_score}] times.')
print("Goodbye!")
sys.exit()

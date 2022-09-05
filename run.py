# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# modify score varible
user_score = 0 
computer_score = 0
options = ["rock", "paper", "scissors"]
user_name = input("Welcome to Rock, Paper, Scissors Game.\nPlease Enter Your Name? ")

def game(user_input):
    """calculate the computer option"""
    random_number = random.randint(0, 2)

    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f'{user_name} picked {user_input} .')
    print(f'Computer picked {computer_pick} .')
    get_result(user_input,computer_pick)
    
    def get_result(user_input,computer_pick):
    """check the result""" 
    global user_score, computer_score
    
    if user_input == computer_pick :
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
user_name=input("enter your name")
Print(user_name)

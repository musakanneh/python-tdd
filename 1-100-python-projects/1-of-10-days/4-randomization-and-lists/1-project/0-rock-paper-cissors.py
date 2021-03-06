#!/usr/bin/python3
"""Rock, Paper, Scissors
Randomly makes a choice b/w rock, paper or scissors
then compares the choice generated by the computer against
the user's choice; then determines the winner - based on the
rock, paper and scissors' game rules
"""

import random


def rock_paper_scissors():
    """Gets users' input and determines winner
    """
    print("Welcome to the Rock, Paper, Scissors game")
    rock = '''
    _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
    paper = '''
        _______
        ---'   ____)____
                ______)
                _______)
                _______)
        ---.__________)
        '''
    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    game_images = [rock, paper, scissors]
    user_choice = int(input(
        "What do you choose? 0 for Rock, 1 for Paper, or 2 for Scissor: "))
    if user_choice >= 3 or user_choice < 0:
        print("You entered an invalid number")
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer choice:{}".format(game_images[computer_choice]))

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose :(")
        elif computer_choice > user_choice:
            print("You lose :(")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")


print(rock_paper_scissors())

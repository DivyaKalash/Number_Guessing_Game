from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Guess Low")
        return turns - 1
    elif guess < answer:
        print("Guess High")
        return turns - 1
    else:
        print("WooHoo! , You guessed it right.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid Input!")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("Computer:I'm thinking of a number between 1 and 100.")
    turns = set_difficulty()
    guess = 0
    answer = randint(1, 100)

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of turns.You lose!")
            return
        elif guess != answer:
            print("Guess Again!")


game()

import random

RANGE = range(1, 101)
MIN = min(RANGE)
MAX = max(RANGE)


def main():
    """
    This is my final project program. Enjoy!
    """
    # List keeps track of number of tries per game, then later picks the
    # lowest value as the "best game"
    best_game = []

    # Greetings
    print("\nWelcome to my Guessing Game! ")

    # This is the answer
    answer = get_number()

    game = True
    while game is True:

        num_tries = play_game(answer)
        if num_tries > 1:
            print(f"It took you {num_tries} guesses.")
        elif num_tries == 1:
            print(f"It only took you {num_tries} guess.")

        response = ask_if_user_wants_to_replay()

        if response == "Y":
            answer = get_number()
            best_game.append(num_tries)
            game = True
        elif response == "N":
            best_game.append(num_tries)
            game = False

    end_of_game(best_game)


def get_number():
    """
    Function generates a random number and displays it
    """

    # Computer will come up with the answer, then display it as per
    # instructor's request
    answer = random.choice(RANGE)
    # print(f"\n(The answer is {answer})")
    return answer


def play_game(answer):
    """
    Function gets guess from the user, then checks if it is too high,
    too low, or if user guessed it. Tracks and then returns the number
    of tries.
    """

    # Initializations
    game = True
    max_num = MAX
    min_num = MIN
    tries = 0

    while game is True:

        try:
            # Collects guess from user
            number = int(input(f"Guess a number between {min_num} and "
                               f"{max_num}: "))
            tries += 1
            game, min_num, max_num = check_nums(min_num, max_num, number,
                                                answer)

        except ValueError:
            print("\nPlease guess a number.\n")
            game = True

    return tries


def check_nums(min_num, max_num, number, answer):
    """
    Function checks the information from play_game() and updates
    min_num and max_num numbers, returning values necessary to update
    the min_num, max_num and whether the loop should execute.
    """
    # Checks values from play_game()
    if min_num <= number <= max_num:
        if number > answer:
            print("Too high!")
            max_num = number
            game = True
        elif number < answer:
            print("Too low!")
            min_num = number
            game = True
        elif number == answer:
            print("You guessed it!")
            game = False
    else:
        print(f"\nYour guess must be between {min_num}" f" and {max_num}.\n")
        game = True

    # game is boolean operator for loop, min_num and max_num set upper and
    # lower boundaries for the game
    return game, min_num, max_num


def ask_if_user_wants_to_replay():
    """
    Function asks user if they want to play again. Forces capital letter,
    checks if it is a correct entry.
    """

    # List of options available to user. Will not accept input unless
    # it is a "Y" or "N"
    options = ["Y", "N"]

    # Loop that gets user's response whether they want to play again.
    response = ""
    while response not in options:
        try:
            response = input("Play again? (Y/N): ").capitalize()
        except ValueError:
            print("Invalid input. Try again.")

    return response


def end_of_game(best_game):
    """
    End of the game process
    """
    # calculate the best game
    best_game = min(best_game)

    # Thanks for playing
    print("\nThanks for playing!")

    # Displays correct grammar
    if best_game == 1:
        print(f"Your best round was {best_game} guess.")
    else:
        print(f"Your best round was {best_game} guesses.")


main()

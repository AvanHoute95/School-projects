import random

# to prevent 'magic' numbers
DIVIDER = '-' * 43
# list for the game
OPTIONS = ['rock', 'paper', 'scissors']
# menu options
MENU = [1, 2]


def main():
    """Welcome! This program runs a friendly game of Rock, Paper, Scissors
    pitting the user against the computer.
    """

    # Greet user
    print("\nLet's play Rock, Paper, Scissors!\n")

    # initiate game by calling function begin_game
    game_on = begin_game()

    # if user wants to play, the game will begin.
    # If not, the program will terminate.
    if game_on is True:
        wins = 0
        losses = 0
        ties = 0
        games = 0
        game_stats = play_game(wins, losses, ties, games)
        game_results(game_stats)
    else:
        print("\nFine then. Thanks for wasting my time.\n")


def begin_game():
    """Asks user if they want to play. 1 or 2 are required inputs."""

    # Begin by asking user if they want to play.
    i = 1
    while i == 1:
        try:
            # an input of 1 or 2 is required.
            play_game = int(input("\nWould you like to play?\n1 = yes\n2 = no"
                                  "\nChoice: "))
            # if play_game in MENU or play_game in ALT_CHOICE:
            if play_game == MENU[0]:
                game_on = True
                i = 2
            elif play_game == MENU[1]:
                game_on = False
                i = 2
            else:
                print()
                print(DIVIDER)
                print("Input must be '1' or '2'. Try again.")
                print(DIVIDER)
                i = 1
        except ValueError:
            print()
            print(DIVIDER)
            print("Hmmm... Something went wrong. Try again.")
            print(DIVIDER)

    # returns user's choice
    return game_on


def get_choice():
    """Prompts user to choose what move they want to make"""
    print()
    print(DIVIDER)
    # Get a choice from the user.
    i = 1
    while i == 1:
        try:
            # input it forced to be lower case to ensure input is correct
            choice = input("Please type 'Rock', 'Paper', or "
                           "'Scissors':\n\n").lower()

            # checks if user's input is in the list of choices for RPS.
            if choice in OPTIONS:
                player_move = choice
                i = 2
            else:
                print(DIVIDER)
                print("Invalid input. Try again.")
                print(DIVIDER)
                print()
                i = 1
        except ValueError:
            print()
            print(DIVIDER)
            print("Hmmm... Something went wrong. Try again.")
            print(DIVIDER)
    # returns player's move choice
    return player_move


def get_computer_choice():
    """Gets move choice from the computer"""

    # get a choice from the computer from the provided list.
    comp_move = random.choice(OPTIONS).lower()

    # returns computer's move choice
    return comp_move


def play_game(wins, losses, ties, games):
    """
    Runs game of Rock, Paper, Scissors. User will be given opportunity to
    quit or rerun. Game stats are incrememented
    """
    # this loop is the game
    i = 1
    while i == 1:

        # run functions to get input from user and computer
        comp_move = get_computer_choice()
        player_move = get_choice()

        # display choices
        print()
        print(DIVIDER)
        print(f"You chose {player_move}.")
        print(f"Computer chose {comp_move}.\n")

        # Logic of the game. Game stats are incrememented
        if player_move == comp_move:
            print("It's a tie!")
            ties += 1
            games += 1
            i = 2
        elif player_move == OPTIONS[0]:
            if comp_move == OPTIONS[1]:
                print(f"{OPTIONS[0].capitalize()} is covered by {OPTIONS[1]}."
                      " You lose!")
                losses += 1
                games += 1
                i = 2
            elif comp_move == OPTIONS[2]:
                print(f"{OPTIONS[0].capitalize()} smashes {OPTIONS[2]}. "
                      "You win!")
                wins += 1
                games += 1
                i = 2
        elif player_move == OPTIONS[1]:
            if comp_move == OPTIONS[0]:
                print(f"{OPTIONS[1].capitalize()} covers {OPTIONS[0]}. "
                      "You win!")
                wins += 1
                games += 1
                i = 2
            elif comp_move == OPTIONS[2]:
                print(f"{OPTIONS[2].capitalize()} cuts {OPTIONS[1]}. "
                      "You lose!")
                losses += 1
                games += 1
                i = 2
        elif player_move == OPTIONS[2]:
            if comp_move == OPTIONS[0]:
                print(f"{OPTIONS[0].capitalize()} smashes {OPTIONS[2]}. "
                      "You lose!")
                losses += 1
                games += 1
                i = 2
            elif comp_move == OPTIONS[1]:
                print(f"{OPTIONS[2].capitalize()} cuts {OPTIONS[1]}. You win!")
                wins += 1
                games += 1
                i = 2
        print(DIVIDER)
        # ask user if they would like to play again
        while i == 2:
            try:
                response = int(input("\nPlay again?\n1 = yes\n2 = no\n\n"
                                     "Choice: "))

                # get user's response
                if response == MENU[0]:
                    i = 1
                elif response == MENU[1]:
                    i = 3
                else:
                    print()
                    print(DIVIDER)
                    print("Input must be '1' or '2'. Try again.")
                    print(DIVIDER)
            except ValueError:
                print()
                print(DIVIDER)
                print("Hmmm... Something went wrong. Try again.")
                print(DIVIDER)

    # when user is done, all stats are returned to be displayed at the end
    game_stats = [wins, losses, ties, games]
    return game_stats


def game_results(game_stats):
    """This function displays the results.
    It is the last function to run before program terminates.
    """

    # assign stats to list values from list results
    wins = game_stats[0]
    losses = game_stats[1]
    ties = game_stats[2]
    games = game_stats[3]

    # display stats to the user.
    print(DIVIDER)
    print("STATS:\n")
    print(f"Games played: {games: 4d}")
    print(f"Human wins: {wins: 6d}")
    print(f"Computer wins: {losses: 3d}")
    print(f"Ties: {ties: 12d}")

    # final silly messages to user, because why not
    if losses > wins and losses >= ties:
        print("\nYou suck, hu-man.")
    if wins > losses:
        print("\nGood job, you beat an inanimate object. Give yourself a big "
              "'ol pat on the back.")
    if wins == losses:
        print("\nWelp, it's a tie.")
    print("\n\n")


main()

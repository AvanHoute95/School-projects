import random

DIVIDER = '*' * 33
TALENT_FILE = "talents.txt"
FIELD = "1"
PASS = "2"
QUIT = "3"
OPTIONS = [FIELD, PASS, QUIT]
LOTS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
DICE_NUMBERS = 6


def main():
    """Main function for the program, calls all other functions needed"""
    # read the account talents
    talents = get_talents(TALENT_FILE)

    # get choice from the user
    if talents > 0:
        choice = get_choice(talents)

        while choice != OPTIONS[2] and talents > 0:
            talents, choice = play_game(talents, choice)

    # End program
    if talents > 0:
        write_talents(talents)

    elif talents <= 0:
        reset_talents()

    print("\nGoodbye.")


def get_choice(talents):
    """Ask user for choice of the menu"""

    # display the amount of talents the user has
    print(f"\nYou have {talents} talents\n")

    # Display menu items to the user
    if talents > 0:
        print("1 - Field Bet")
        print("2 - Pass Bet")
        print("3 - Quit")

        # Loop checks that input is in the menu parameters
        choice = ""
        while choice not in OPTIONS:
            choice = input("Choice: ")

    elif talents <= 0:
        # reset_talents()
        choice = LOTS[2]

    return choice


def get_talents(filename):
    """gets the talents from the txt file"""

    # read talents.txt and convert string to int.
    talents = 0
    try:
        talents_file = open(filename)
        talents = int(talents_file.read())
        talents_file.close()

    except ValueError:
        print("\nFile does not contain a valid value for talents.\n")

    except IOError:
        print(f"\nCannot read from the file: {filename}")

    return talents


def get_wager():
    """This function gets the wager from the user"""

    # collects input from the user that is the amount of talents
    # they want to wager
    print()

    wager = ""
    i = True
    while i is True:
        try:
            wager = int(input("How much would you like to wager? "))
            if wager > 0:
                i = False
            elif wager < 0:
                print("You must wager more than 0.")
                i = True
        except ValueError:
            print("Oopsie woopsie something went wrong.")
            i = True

    return wager


def play_game(talents, choice):
    """Function is the core of the game"""

    i = 1
    while i == 1:

        wager = get_wager()
        roll = str(random.randint(1, DICE_NUMBERS) +
                   random.randint(1, DICE_NUMBERS))

        if talents >= wager:

            # Field bet
            if choice == OPTIONS[0]:
                talents = field_bet(roll, wager, talents)
                choice = get_choice(talents)
                i = 2

            # Pass bet
            elif choice == OPTIONS[1]:
                talents = pass_bet(roll, wager, talents)
                choice = get_choice(talents)
                i = 2

        else:
            print("You don't have enough talents to make that bet.")
            i = 1

    return talents, choice


def field_bet(roll, wager, talents):
    """This function is the FIELD BET function"""

    # show the roll
    print(f"The LOTS CAST is{roll:.>17}")

    # if roll is 2 or 12 then user wins double their bet
    if roll == LOTS[0] or roll == LOTS[10]:
        talents = (talents + (wager * 2))
        print("You won double your bet.")

    # if roll is 3, 4, 9, 10, or 11 then user wins even talents
    elif roll == LOTS[1] or roll == LOTS[2] or roll == LOTS[7] or \
            roll == LOTS[8] or roll == LOTS[9]:
        talents = talents + wager
        print(f"You won {wager} talents.")

    # if roll is 5, 6, 7, or 8 then user loses their bet
    elif roll == LOTS[3] or roll == LOTS[4] or roll == LOTS[5] or \
            roll == LOTS[6]:
        talents = talents - wager
        print("You lost your bet.")

    return talents


def pass_bet(roll, wager, talents):
    """This function is the pass bet function"""

    # Display to user the dice value
    print(f"The LOTS CAST is{roll:.>17}")

    # Lose bet if roll is 2 or 12
    if roll == LOTS[0] or roll == LOTS[10]:
        talents = talents - wager
        print("You lost your bet.")

    # win back your wager if roll is 7 or 11
    elif roll == LOTS[5] or roll == LOTS[9]:
        talents = talents + wager
        print("You won even talents.")

    # cast becomes POINT if roll is 3, 4, 5, 6, 8, 9, or 10
    elif roll == LOTS[1] or roll == LOTS[2] or roll == LOTS[3] or \
            roll == LOTS[4] or roll == LOTS[6] or roll == LOTS[7] or \
            roll == LOTS[8]:

        # set point equal to the roll value then call point roll function
        print("\nCast becomes POINT.")
        point = roll
        talents = cast_becomes_point(point, talents, wager)

    return talents


def cast_becomes_point(point, talents, wager):
    """Function is called when cast becomes POINT"""

    # roll dice until you get 7, 11, or the POINT value
    i = 1
    while i == 1:
        point_roll = str(random.randint(1, DICE_NUMBERS) +
                         random.randint(1, DICE_NUMBERS))

        print(f"The LOTS CAST is{point_roll:.>17}")

        # 7 or 11: lose your bet
        if point_roll == LOTS[5] or point_roll == LOTS[9]:
            print("You lost your bet")
            talents = talents - wager
            i = 2

        # POINT: win even with wager
        elif point_roll == point:
            print("You won even talents")
            talents = talents + wager
            i = 2

    return talents


def write_talents(talents):
    """Writes the new talents to the file when user exits the game"""

    # write talents from game to talents.txt to be read later
    try:
        talents_file = open(TALENT_FILE, "w")
        talents_file.write(str(talents))
        talents_file.close()

    except IOError:
        print("Cannot write to the file.")

    print(f"\nTalents saved! ({talents})")


def reset_talents():
    """Writes the new talents to the file"""

    print("You don't have any talents to play with.\n")
    print("You will have 100 talents next time you play.")

    # if user runs out, re-write the talents to 100.
    if TALENT_FILE == "talents.txt":
        try:
            talents_file = open(TALENT_FILE, "w")
            talents_file.write(str(100))
            talents_file.close()

        except IOError:
            print("Cannot write to the file.")


main()

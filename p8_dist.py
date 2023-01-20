HOUR = 10
BIG_HOUR = 100


def main():
    """This program will collect speed and hours traveled,
    in integers, then display the distance traveled
    based on the entered information. """

    # greet
    print("Welcome!\n")

    # call function to get data
    speed, hours = get_data()

    # this function calculates then calls a response function
    calc_dist(speed, hours)


def get_data():
    """Get input from user then returns values and continues program"""

    # Collect speed from user.
    speed = None
    while speed is None:
        speed = int(input("Enter vehicle speed (mph): "))
        if speed == 0:
            print("Speed can't be zero.")
            speed = None
        elif speed < 0:
            print("You must enter a positive number.")
            speed = None

    # collect hours from user
    hours = None
    while hours is None:
        hours = int(input("Enter the hours traveled:  "))
        if hours == 0:
            print("Hours can't be zero.")
            hours = None
        elif hours < 0:
            print("You must enter a positive number.")
            hours = None

    # return the values, go back to main
    return speed, hours


def calc_dist(speed, hours):
    """Displays and calculates data"""

    # display distance traveled at given speed
    print("\nHours       Distance (miles)")
    print("----------------------------")
    i = 1
    for hours in range(1, hours + 1):
        if hours < HOUR:
            print(f"{hours} {speed * hours: 26d}")
        elif HOUR <= hours < BIG_HOUR:
            print(f"{hours} {speed * hours: 25d}")
        elif hours >= BIG_HOUR:
            print(f"{hours} {speed * hours: 24d}")
        i += 1

    # call function to ask user if they want to go again from the top
    response()


def response():
    """This function asks user if they want to run the program again"""

    # ask the question

    # Collects input from user. Y, y, N, or n.
    answer = None
    while answer is None:
        answer = input("\nRun Again? (Y/N): ")
        if answer == 'y' or answer == 'Y':
            # if user says yes, rerun the program from the top
            main()
        elif answer == 'n' or answer == 'N':
            # if no, exit program.
            print("\nGoodbye.")
        else:
            print("Invalid input. Follow instructions.")
            answer = None


main()

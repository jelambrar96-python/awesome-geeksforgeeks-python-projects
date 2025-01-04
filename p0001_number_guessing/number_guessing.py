import math
import random

def main():
    # Taking Inputs
    lower = int(input("Enter Lower bound: "))

    # Taking Inputs
    upper = int(input("Enter Upper bound: "))

    # Seed the random number generator
    random.seed()

    # Generating random number between the lower and upper
    x = random.randint(lower, upper)
    total_chances = math.ceil(math.log(upper - lower + 1) / math.log(2))

    print("\n\tYou've only {} chances to guess the integer!\n".format(total_chances))

    # for calculation of minimum number of guesses depends
    # upon range
    count = 0
    flag = 0
    while count < total_chances:
        count += 1

        # Taking guessing number as input
        guess = int(input("Guess a number: "))

        # Condition testing
        if x == guess:
            print("Congratulations you did it in {} try!".format(count))
            # Once guessed, loop will break
            flag = 1
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You guessed too high!")

    # If Guessing is more than required guesses, shows this
    # output.
    if not flag:
        print("\nThe number is {}".format(x))
        print("\tBetter Luck Next time!")

if __name__ == "__main__":
    main()
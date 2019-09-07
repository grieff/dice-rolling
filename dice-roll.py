# Dice Rolling Simulation
# Python 3.0

# Rolls a number of dice, with x sides, depending on the user input

import random

# ROLL FUNCTION
def roll(die, sides):
    r = 0
    # While loop based on number of dice selected
    while r < die:
        # Store the random roll to variable rolls
        rolls = random.randint(1, sides)
        # Increase r by 1 each loop
        r += 1
        # Prints out the rolls for each die selected
        print("Rolled a ", rolls)

# MAIN FUNCTION
def main():
    rolling = True
    # start loop
    while rolling:
        # Receive an anser to begin the program
        answer = input("Ready to roll? Y or N:")
        # If user says yes, run the program
        if answer.lower() == "y"
            # Variable for amount of die
            die = eval(input("Please enter the amount of dice you wish to roll"))
            # Variable for amount of sides
            sides = eval(input("Please enter the number of sides on your dice:"))
        else:
            print("Thank you for playing")
            # End while loop
            break

# Call main function
main()
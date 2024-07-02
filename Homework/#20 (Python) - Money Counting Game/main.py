# Money Counting Game (Program 3-10)
# 3/19/2021
# About 10-15 minutes

# Declaring Variables
pennies = 0
nickels = 0
dimes = 0
quarters = 0
compositeScore = 0

# Asking for values
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarter: "))

# Math
nickels = nickels * 5
dimes = dimes * 10
quarters = quarters * 25

compositeScore = pennies + nickels + dimes + quarters
# output
if compositeScore < 0:
    print("Sorry, the amount you entered was less than a dollar, and" \
    " negative as well.")
elif (0 <= compositeScore < 100):
    print(" Sorry, the amount you entered was less than one dollar.")
elif compositeScore == 100:
    print("Congratulations!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!")
elif compositeScore > 100:
    print("Sorry, the amount you entered was more than one dollar.")

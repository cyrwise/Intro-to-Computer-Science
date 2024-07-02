# Sales Bonus (Jv S21)
# 3/19/2021
# About 15-20 minutes because I accidentally closed the tab on my first
# attempt

# Declaring variables
salesAmount = 0.0

# Input for sales amount
salesAmount = float(input("Enter the dollar amount" \
" of sales this month: "))

# Output for negative result
if salesAmount < 0:
    print("Negative sales? Forget the bonus, you're fired!")
    
# Regular output
if (0 <= salesAmount <= 500000):
    print("Sorry, but there is no bonus available for you. Better" \
    " luck next time!")
elif (500000 < salesAmount <= 1000000):
    print("Congratulations! You have earned a bonus of $1000.")
elif salesAmount > 100000:
    print("Congratulations! You are going on a free trip to Hawaii!" \
    " Keep up the great work!")
# I put over 1 million only to fit the request of the prompt

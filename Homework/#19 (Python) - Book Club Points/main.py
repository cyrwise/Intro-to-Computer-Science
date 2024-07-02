# Book Club Points (Program 3-11)
# 3/19/2021
# About 10-15 minutes to make and test

# Declaring variables 
booksPurchased = 0
# Removed points as a variable

# Input for books purchased
booksPurchased = int(input("Enter the number of books" \
" purchased this month: "))

# Output error (not sure if this is necessary but its fun to add)
if booksPurchased < 0:
    print("Invalid number entered: books purchased" \
    " cannot be negative.")
    
# Output (points awarded)
if booksPurchased == 0 or booksPurchased == 1:
    print("You have purchased", booksPurchased, "books this month.")
    print("This earns you 0 points.")
elif booksPurchased == 2 or booksPurchased == 3:
    print("You have purchased", booksPurchased, "books this month.")
    print("This earns you 5 points.")
elif booksPurchased == 4 or booksPurchased == 5:
    print("You have purchased", booksPurchased, "books this month.")
    print("This earns you 15 points.")
elif booksPurchased == 6 or booksPurchased == 7:
    print("You have purchased", booksPurchased, "books this month.")
    print("This earns you 30 points.")
elif booksPurchased >= 8:
    print("You have purchased", booksPurchased, "books this month.")
    print("This earns you 60 points. Congratulations!")

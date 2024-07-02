# MPG (2-7) Solution
# 2/18/2021
# About 20-25 minutes

# Declare real miles, gallons, mpg
miles = 0.0
gallons = 0.0
mpg = 0.0

# Display an input for enter miles driven
miles = float(input("Enter the miles driven: "))

# Display an input for gallons of fuel used
gallons = float(input("Enter the gallons of fuel used: "))

# Put in the formula
mpg = miles/gallons

# Display mpg value to user
print("You got", format(mpg, '.2f'), "miles per gallon.")

# I got the code above from checking the solution, what I wrote previously waas
# print("You got", mpg, "miles per gallon.")
# From my understanding, the .2f part is having the two spots after the
# decimal mark for a more accurate value.
# Other than that, my answers were the same as the solution.

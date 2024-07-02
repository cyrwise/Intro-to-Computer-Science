# Pennies for Pay 4-7
# Today is 3/25/2021
# It took around 15-20 minutes to complete

# Variables
salary = 0.005
# Made it 0.005 to compensate for starting at 1 from the loop \
# statement

# input (number of days)
numberOfDays = int(input("Enter the number of days: "))

# Setting up the table (I found out how to make a proper table since \
# the one I used in the last problem felt off)
print("\nDay\t Pennies\n========================")

# loop statement
# This took me the most amount of time mainly because I forgot a
# second parentheses in line 12
for day in range(1, numberOfDays+1, 1):
    salary *= 2
    print(day, "\t", "$", format(salary, ",.2f"))
    
salary *= 2    
print("The total salary for", numberOfDays, "is: $", salary)
# I am not sure why the sample run multiplies the end value
# by two, but I added that to the program to match the result.

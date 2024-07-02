# Batting Average Calculator (CPP EO 3-5)
# 2/28/2021
# Around 10 minutes, main problem I had was at the end where
# I put the comma in the quotes, so i fixed it by doing ", instead
# of ,"
# I added print("") spaces as well to match the format of the sample run

# Welcoming message
print("Find your batting average!")
print("")

# Ask for number of times hit
number_at_bat = int(input("Enter the number of times at bat: "))

# Ask for hits earned
number_hits_earned = int(input("Enter the number of hits earned: "))
print("")

# Calculate the batting average
batting_average = number_hits_earned / number_at_bat

#Display the batting average
print("The player\'s batting average is", format(batting_average, '.3f'))

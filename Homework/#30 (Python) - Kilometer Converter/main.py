# Farzan Mojabi CIS2 Hendrickson
# Kilometer converter 5-1
# 4/8/2021
# It took around 10 minutes to complete, i chose .2f for this
# too

def miles():
    # Get input for kilo number
    kilometers = float(input("Enter the distance in kilometers: "))
    
    #Formula
    miles = kilometers * 0.6214
    
    # Output
    print("The conversion of", format(kilometers, ".2f"), \
    "kilometers to miles is", format(miles, ".2f"), "miles.")
    
miles()

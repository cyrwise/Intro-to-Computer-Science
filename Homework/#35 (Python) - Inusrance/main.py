# Insurance (Farrell 8th J 3-9 S21)
# 4/16/2021
# It took me about 15-20 minutes, since I realized I needed to add
# the math module in, and I had to learn how to use it for this
# problem alongside that.

# Import math module
import math
# Aes = Aesthetics

def main():
    
    # Opening Message
    print("Harrison Group Life")
    print("Annual Insurance Premium Calculator")
    
    # Aes
    print("")
    
    # Ask for current Year
    current_year = int(input("Enter the current year: "))
    birth_year = int(input("Enter your birth year: "))
    
    # Aes
    print("")
    
    # Pass to other function to calculate premium
    premium = calculator(current_year,birth_year)
    
    # Give output
    print("Your annual premium will be $", premium,".")
    
    
def calculator(current_year,birth_year):
    
    # Math
    age = current_year - birth_year
    numOfDecades = age/10
    numOfDecades = math.floor(numOfDecades)
    
    calcPremium = (numOfDecades + 15) * 20
    
    return calcPremium

    
# Call main function    
main()

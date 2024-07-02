# Metric Conversion (Farrell 8th J 3-7)
# 4/10/2021
# It took about: 7-10 minutes, I think I've got the hang of passing
# arguments by now. :)

def main():
    userNumber = float(input("Enter a number to convert inches" \
    " to centimeters and gallons to liters: "))
    asInchesToCentimeters(userNumber)
    
def asInchesToCentimeters(unAsInches):
    final_Centimeters = unAsInches * 2.54
    print(unAsInches, "inches is", final_Centimeters, "centimeters")
    asGallonsToLiters(unAsInches)
    
def asGallonsToLiters(unAsGallons):
    final_Liters = unAsGallons * 3.7854
    print(unAsGallons, "gallons is", final_Liters, "liters")
    
main()

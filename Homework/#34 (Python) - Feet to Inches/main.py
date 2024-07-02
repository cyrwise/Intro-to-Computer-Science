# Feet to Inches 5-10
# 4/16/2021
# It took me about 10-15 minutes to complete this.


def main():
    inputFeet = float(input("Enter the number of feet: "))
    inchesMain = feet_to_inches(inputFeet)
    print(inputFeet, "feet =", format(inchesMain,".2f"), \
    "inches")

def feet_to_inches(inputFeet):
    inches = inputFeet*12
    return inches
    

    
# call main function
main()

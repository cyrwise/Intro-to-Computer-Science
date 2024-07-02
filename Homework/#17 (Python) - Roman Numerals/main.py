# Roman Numerals (Program 3-4)
# 3/13/2021
# Around 7-10 minutes

# Declaring variables
userNumber = 0.0

# Input for number
userNumber = int(input("Enter an exact number between 1 and 10" \
" to be converted: "))

# Output (error messages)
if userNumber>10:
    print("Invalid number entered: Specified value cannot" \
    " be greater than 10.")
elif userNumber<1:
    print("Invalid number entered: Specified value cannot" \
    " be less than 1.")
    
# Output (Roman numerals)
elif userNumber==1:
    print("I")
elif userNumber==2:
    print("II")    
elif userNumber==3:
    print("III")
elif userNumber==4:
    print("IV")
elif userNumber==5:
    print("V")
elif userNumber==6:
    print("VI")
elif userNumber==7:
    print("VII")
elif userNumber==8:
    print("VIII")
elif userNumber==9:
    print("IX")
elif userNumber==10:
    print("X")

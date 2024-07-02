# Day of the week (program 3-1)
# 3/13/2021
# Around 10 minutes, I wasn't sure how I was supposed to display
# the corresponding day, so I just put the day itself based on
# the prompt.

# Declaring variables
userNumber = 0.0

# input for number
userNumber = int(input("Enter an exact number between 1 to 7: "))

# Output (error messages)
if userNumber>7:
    print("Invalid number entered: Specified value cannot be greater" \
    " than 7.")
elif userNumber<1:
    print("Invalid number entered: Specified value cannot be less" \
    " than 1.")

# Output (corresponding day of the week)
elif userNumber==1:
    print("Monday")
elif userNumber==2:
    print("Tuesday")
elif userNumber==3:
    print("Wednesday")
elif userNumber==4:
    print("Thursday")
elif userNumber==5:
    print("Friday")
elif userNumber==6:
    print("Saturday")
elif userNumber==7:
    print("Sunday")

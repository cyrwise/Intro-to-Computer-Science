# Age Classifier (program 3-3)
# 3/13/2021
# Around 10 minutes, I used int values for this since it
# seemed more appropriate.

# declaring variables (for convenience)
age = 0.0

# asking for age
age = int(input("Enter the age of the person: "))

# Age classification and output
if age<0:
    print("Invalid age entered: Specified value cannot be under" \
    " 0 years of age.")
elif age<=1:
    print("The person is an infant (Being 1 or younger).")
elif age<13:
    print("The person is a child.")
elif age<20:
    print("The person is a teenager.")
else:
    print("The person is an adult.")

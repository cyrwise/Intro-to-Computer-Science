# Dog years (Jv S21)
# 3/13/2021
# Around 7-10 minutes, I used int values and made this relative 
# to aunt Suzy's age instead of asking for age because I don't 
# think im being asked to do that

# Declaring variables
AUNT_AGE = 47
dogAge = 0.0

# Ask for dog age (input)
dogAge = int(input("Enter the age of your dog in human years: "))
    
# matheeymatrixs
dogAge = dogAge*7

# Output (error)
if dogAge<0:
    print("Invalid age entered: Specified value cannot" \
    " be a negative number.")

# Output (regular)
elif dogAge>AUNT_AGE:
    print("You are younger than the dog.")
elif dogAge<AUNT_AGE:
    print("You are older than the dog.")
    
# just realized this isn't even possible with int values haha
elif dogAge==AUNT_AGE:
    print("You are the same age as the dog.")

# In between (Farrell Jv 9e 6-4 S21)
# 3/25/2021
# About 10-15 minutes, while doing this problem it felt as
# if my learning finally clicked :)

# Asking for the two integers
intOne = int(input("Enter an integer value: "))
intTwo = int(input("Enter a second integer value: "))

# Output if no integers
if intTwo == intOne + 1 or intOne == intTwo + 1 or intTwo == intOne:
    print("No integers exist between the entered values.")

# Other output loop (works despite which one is larger)
elif intOne < intTwo:
    while intOne < intTwo - 1:
        intOne += 1
        print(intOne)
elif intTwo < intOne:
    while intTwo < intOne - 1:
        intTwo += 1
        print(intTwo)

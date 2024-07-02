# Calories burned 4-2
# 3/25/2021
# Around 10 minutes; I feel like my approach worked however
# I am not sure it is supposed to be 237 steps. I did it from
# What I learned in the lesson though.

# variables
minutes = 0
while minutes<30:
    minutes += 1
    total = minutes*4.2
    if minutes == 10:
        print("You have burned", total, "calories in 10 minutes!")
    elif minutes == 15:
        print("You have burned", total, "calories in 15 minutes!")
    elif minutes == 20:
        print("You have burned", total, "calories in 20 minutes!")
    elif minutes == 25:
        print("You have burned", total, "calories in 25 minutes!")
    elif minutes == 30:
        print("You have burned", total, "calories in 30 minutes!")

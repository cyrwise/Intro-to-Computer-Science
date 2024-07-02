# Distance traveled program 4-4
# 3/25/2021
# About 15 minutes, this one was more tricky

# input
speed = int(input("What is the speed of the vehicle in mph?: "))
time = int(input("How many hours has it traveled?: "))

# Making the output pretty (to match similarly to the table)
print()
print("Hour","      Distance Traveled")

# looping statement
for hour in range (1, time + 1):
    distance = speed*hour
    
    # Final output
    print(hour, "        ", distance)

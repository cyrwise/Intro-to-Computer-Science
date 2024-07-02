# Bug collector program 4-1
# 3/25/2021
# About 10-15 minutes

# total variable
total = 0

# loop
for day in range(1, 6):
    
    #input
    print("Enter the number of bugs collected on day", day)
    bugs = int(input())
    
    # math
    total += bugs
    
# final display
print("Total bugs collected: ", total)

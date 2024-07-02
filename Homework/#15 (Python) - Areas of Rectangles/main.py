# Areas of Rectangles (program 3-2)
# 3/13/2021
# around 10-15 minutes, it was fun to do as well

# declaring variables
width1 = 0.0
length1 = 0.0
width2 = 0.0
length2 = 0.0

# ask for length and width of two rectangles
width1 = float(input("Enter the width of the first rectangle: "))
length1 = float(input("Enter the length of the first rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))
length2 = float(input("Enter the length of the second rectangle: "))

# matheymateecs
area1 = width1 * length1
area2 = width2 * length2

# output calculation
if area1>area2:
    print("Rectangle 1 has the greatest area at", format(area1, '.2f'), \
    "units.")
elif area2>area1:
    print("Rectangle 2 has the greatest area at", format(area2, '.2f'), \
    "units.")
else:
    print("Rectangle 1 and 2 have the same area at", format(area2, '.2f'), \
    "units.")

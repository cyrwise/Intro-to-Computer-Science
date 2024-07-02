# Hypnotic Pattern
# 3/30/2021
# Spent: about 7-10 minutes, it was mainly about finding
# the loop.

import turtle
turtle.speed(0)
turtle.hideturtle

# Vars
goLength = 5

# Loop
for times in range (50):
  turtle.forward(goLength)
  turtle.left(90)
  goLength += 5

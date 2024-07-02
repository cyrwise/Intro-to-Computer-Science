# Starting
import turtle
turtle.speed(0)
turtle.hideturtle()

# Dotted line plan: long side = 200, short = 
# 141.421356237
# 0-15, 45-85, 115-155, 185-200
turtle.dot()
turtle.setheading(135)
turtle.forward(141.421356237)
turtle.dot()

# top dotted segment
turtle.setheading(0)
turtle.forward(20)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(20)
turtle.dot()

# setting up other lines
turtle.setheading(-90)
turtle.forward(200)
turtle.dot()

turtle.setheading(135)
turtle.forward(141.421356237)

turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(-100,-100)
turtle.dot()
turtle.goto(-100,100)

turtle.penup()
turtle.goto(-100,-100)

# Final dotted line
turtle.pendown()
turtle.setheading(0)
turtle.forward(20)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(20)

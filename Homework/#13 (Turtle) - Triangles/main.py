import turtle
turtle.speed(0)
# hide turtle goes here
turtle.hideturtle()
# first golden triangle
turtle.fillcolor('gold')
turtle.begin_fill()
turtle.setheading(-45)
turtle.forward(100)
turtle.setheading(-180)
turtle.forward(141.421356237)
turtle.setheading(45)
turtle.forward(100)
turtle.end_fill()

# outer triangle
turtle.setheading(-45)
turtle.forward(100)
# 90-45 /2 = 22.5
# 90 + 22.5 = 112.5
turtle.setheading(116.35)
turtle.forward(160)
turtle.setheading(-116.35)
turtle.forward(160)

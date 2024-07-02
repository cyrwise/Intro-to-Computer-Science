import turtle
turtle.speed(0)
turtle.circle(50)
turtle.hideturtle()

# main ring is now set so I put in the side rings
# starting with right side rings
turtle.penup()
turtle.goto(60,-50)
turtle.pendown()
turtle.circle(50)

# final right side ring
turtle.penup()
turtle.goto(120,0)
turtle.pendown()
turtle.circle(50)

#left side rings
turtle.penup()
turtle.goto(-60,-50)
turtle.pendown()
turtle.circle(50)

#final left ring
turtle.penup()
turtle.goto(-120,0)
turtle.pendown()
turtle.circle(50)

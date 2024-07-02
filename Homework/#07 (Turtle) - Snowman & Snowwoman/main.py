# cis2 hendrickson
# spent: 20-30 minutes

# starting
import turtle
turtle.speed(0)
turtle.hideturtle()

# second ball
turtle.circle(60)

turtle.penup()
turtle.goto(0,80)
turtle.pendown()
turtle.fillcolor('grey')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(0,20)
turtle.pendown()
turtle.fillcolor('grey')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# bottom snowball (legs)
turtle.penup()
turtle.goto(0,-180)
turtle.pendown()
turtle.circle(90)

turtle.penup()
turtle.goto(0,-60)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-130)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# head
turtle.penup()
turtle.goto(0,120)
turtle.pendown()
turtle.circle(40)
# eyes
turtle.penup()
turtle.goto(-15,160)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(4)
turtle.end_fill()
#eye 2
turtle.penup()
turtle.goto(15,160)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(4)
turtle.end_fill()
#mouth
turtle.penup()
turtle.goto(-13,140)
turtle.pendown()
turtle.pencolor('red')
turtle.goto(13,140)

turtle.penup()
turtle.goto(-13,140)
turtle.pendown()
turtle.goto(-22, 148)

turtle.penup()
turtle.goto(13,140)
turtle.pendown()
turtle.goto(22, 148)

#hat
turtle.penup()
turtle.pensize(5)
turtle.pencolor('maroon')
turtle.goto(50,185)
turtle.pendown()
turtle.goto(-50,185)
# top rectangle
turtle.penup()
turtle.fillcolor('maroon')
turtle.begin_fill()
turtle.goto(30,185)
turtle.pendown()
turtle.goto(30,250)
turtle.goto(-30,250)
turtle.goto(-30,185)
turtle.end_fill()

# arms
turtle.penup()
turtle.goto(-40,80)
turtle.pendown()
turtle.goto(-150,90)

# arms 
turtle.penup()
turtle.goto(50,80)
turtle.pendown()
turtle.goto(160, 120)

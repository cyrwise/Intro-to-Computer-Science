# I am not sure if I am supposed to put in
# a header with class name, my name, and other
# information like on the previous assignments we
# did. Also, I think that this one might be
# offset a little but I made it match the photo

# I also skipped animation on all of them

# Starting
import turtle
turtle.speed(0)
turtle.hideturtle()

# middle circle
turtle.goto(0,0)
turtle.circle(50)

# North and line
turtle.setheading(90)
turtle.forward(200)
turtle.penup()
turtle.goto(-20,210)
turtle.pendown()
turtle.write('North', align='central', font=('arial', 14, 'normal'))

# West and line
turtle.penup()
turtle.goto(0,50)
turtle.pendown()

turtle.setheading(180)
turtle.forward(150)
turtle.penup()
turtle.goto(-200,45)
turtle.pendown()
turtle.write('West', align='central', font=('arial', 14, 'normal'))

# South and line
turtle.penup()
turtle.goto(0,50)
turtle.pendown()

turtle.setheading(-90)
turtle.forward(150)
turtle.penup()
turtle.goto(-24,-119)
turtle.pendown()
turtle.write('South', align='central', font=('arial', 14, 'normal'))

# East and line
turtle.penup()
turtle.goto(0,50)
turtle.pendown()

turtle.setheading(0)
turtle.forward(150)
turtle.penup()
turtle.goto(160,45)
turtle.pendown()
turtle.write('East', align='central', font=('arial', 14, 'normal'))

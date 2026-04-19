import turtle

t = turtle.Turtle()
t.speed(2)

# Blue
t.penup()
t.goto(-150, 0)
t.pendown()
t.color("blue")
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

# White
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("white")
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

# Red
t.penup()
t.goto(50, 0)
t.pendown()
t.color("red")
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

turtle.done()
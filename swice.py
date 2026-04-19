import turtle

t = turtle.Turtle()
t.speed(0)

# Red background
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("red")
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Vertical white
t.penup()
t.goto(-20, -60)
t.pendown()
t.color("white")
t.begin_fill()
for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(120)
    t.left(90)
t.end_fill()

# Horizontal white
t.penup()
t.goto(-60, -20)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(120)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()

turtle.done()
import turtle

t = turtle.Turtle()
t.speed(0)

# Blue background
t.penup()
t.goto(-150, -100)
t.pendown()
t.color("blue")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

# White X
t.color("white")
t.width(10)

t.penup()
t.goto(-150, -100)
t.pendown()
t.goto(150, 100)

t.penup()
t.goto(-150, 100)
t.pendown()
t.goto(150, -100)

turtle.done()
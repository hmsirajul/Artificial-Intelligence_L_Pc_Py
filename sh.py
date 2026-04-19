import turtle

t = turtle.Turtle()

t.left(60)
for _ in range(2):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(60)

turtle.done()
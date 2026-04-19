import turtle
t = turtle.Turtle()

t.penup()
t.backward(200)
t.pendown()

width = 400
height = 240

t.fillcolor("green")
t.begin_fill()

for i in range(2):
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
t.end_fill()

t.penup()
t.forward(275)
t.left(90)
t.forward(120)
t.pendown()

t.fillcolor("red")
t.begin_fill()
t.circle(80)
t.end_fill()
turtle.mainloop()
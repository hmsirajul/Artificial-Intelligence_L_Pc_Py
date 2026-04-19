import turtle
t = turtle.Turtle()

t.penup()
t.backward(600)
t.pendown()

t.fillcolor("green")
t.begin_fill()

for i in range(2):
  t.forward(400)
  t.left(90)
  t.forward(200)
  t.left(90)
t.end_fill()

turtle.mainloop()
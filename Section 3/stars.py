import turtle

t = turtle.Turtle()
t.speed("fastest")
t.color("yellow")
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()
turtle.mainloop()

from sketchpy import canvas
import turtle


t = turtle.Turtle()
t.speed(0)
t.hideturtle()


t.penup()
t.goto(-300, 300)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.forward(600)
    t.right(90)
t.end_fill()


t.penup()
t.goto(0, 100)
t.pendown()
t.pensize(5)
t.color("navy")
for _ in range(24):
    t.forward(75)
    t.backward(75)
    t.left(15)


obj = canvas.sketch_from_svg(r"C:\Users\Lenovo\Downloads\2023_07_30.svg")
obj.draw()

turtle.done()

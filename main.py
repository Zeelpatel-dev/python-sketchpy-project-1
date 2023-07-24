import turtle
from sketchpy import library as lib

screen = turtle.Screen()
screen.bgcolor("blue")

web = turtle.Turtle()
web.speed(0)
web.penup()
web.goto(-200, 150)
web.pendown()

for i in range(72):
    web.goto(-200, 150)
    web.right(5)
    web.forward(150)

web.penup()
web.goto(-275, 125)
web.pendown()
for i in range(180):
    web.right(5)
    web.forward(2.5)

obj = lib.tom_holland()
obj.draw()
turtle.exitonclick()

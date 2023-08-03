from sketchpy import library as lib
import turtle
from sketchpy import canvas


screen = turtle.Screen()
screen.bgcolor("blue")


chakra = turtle.Turtle()
chakra.speed(0)
chakra.penup()
chakra.setpos(-50, 100)
chakra.pendown()


chakra.pensize(2)
chakra.pencolor("yellow")
for i in range(24):
    chakra.forward(60)
    chakra.backward(60)
    chakra.left(15)


chakra.hideturtle()


obj = canvas.sketch_from_image(r"C:\Users\Lenovo\Downloads\24052021104050zzq0.jpg")
obj.draw(threshold=127)


turtle.mainloop()


#obj = lib.rdj()
#obj.draw()

#from sketchpy import library
#myObject = library.ironman_ascii()
#myObject.draw()

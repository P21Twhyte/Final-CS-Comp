# Authors: MS 5/10/21

import turtle

window = turtle.Screen()
turtle = turtle.Turtle()

window.setup(700, 700)
window.title("Matching Game")
turtle.penup()
turtle.goto(-125, 300)
turtle.pendown()

for x in range(4):
    turtle.forward(250)
    turtle.right(90)






window.mainloop()


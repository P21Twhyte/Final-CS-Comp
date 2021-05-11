# Authors: MS 5/10/21

import turtle

window = turtle.Screen()
rectangle = turtle.Turtle()

window.setup(1000, 1000)
window.title("Matching Game")

rectangle.forward(250)
rectangle.right(90)
rectangle.forward(100)
rectangle.right(90)
rectangle.forward(250)
rectangle.right(90)
rectangle.forward(100)

window.mainloop()
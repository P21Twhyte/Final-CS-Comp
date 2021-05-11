# Authors: TOW 5/10/21

import turtle

window = turtle.Screen()
square = turtle.Turtle()

square_gif = open("Square.gif")
turtle.register_shape("Square.gif")
square.shape("Square.gif")

window.mainloop()


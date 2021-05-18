import turtle

t = turtle.Turtle()
window = turtle.Screen()
window.title("onclick test")
window.setup(700, 700)


t.color("blue")
t.pensize (40)
t.shape("circle")

window.onclick(t.goto)

#def answer():
    #if turtle.onwindowclick(answer, btn=1, add=true):



window.mainloop()

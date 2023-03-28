import turtle as h

h.pensize(10)
h.pencolor('red')
h.speed(10)
h.bgcolor('black')

def curve():
    for i in range(200):
        h.right(1)
        h.forward(1)

def heart():
    h.fillcolor('red')
    h.begin_fill()
    h.left(140)
    h.forward(113)
    curve()
    h.left(120)
    curve()
    h.forward(112)
    h.end_fill()

heart()
h.pencolor('black')
h.penup()
h.goto(0,170)
h.pendown()

for u in range(3):
    h.left(75)
    h.forward(40)
    h.right(65)
    h.forward(40)

h.ht
h.done()
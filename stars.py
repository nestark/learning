from cir_example import star
import turtle
import math
bobo=turtle.Turtle()
a=100 #height
b=190 #width
c=7/13*a #strip height
d=76
e=c/10
g=d/12
r=3.08
l=r*math.sin((36/180)*math.pi)/math.sin((54/180)*math.pi)
bobo.pencolor('red')
bobo.fillcolor('red')
bobo.speed(10)
bobo.hideturtle()
for i in range(7):
    bobo.begin_fill()
    bobo.forward(b)
    bobo.right(90)
    bobo.forward(a/13)
    bobo.right(90)
    bobo.forward(b)
    bobo.right(90)
    bobo.forward(a/13)
    bobo.end_fill()
    bobo.pu()
    bobo.backward(2*a/13)
    bobo.right(90)
    bobo.pd()
bobo.pu()
bobo.goto(0,0)
bobo.pencolor('blue')
bobo.fillcolor('blue')
bobo.pd()
bobo.begin_fill()
bobo.forward(d)
bobo.right(90)
bobo.forward(7/13*a)
bobo.right(90)
bobo.forward(d)
bobo.right(90)
bobo.forward(7/13*a)
bobo.end_fill()
bobo.right(90)
bobo.pencolor('white')
bobo.fillcolor('white')
for i in range(9):
    bobo.pu()
    bobo.right(90)
    if i==0:
        bobo.forward(e-r)
    else:
        bobo.forward(e)
    if i in range(0,9,2):
        bobo.left(90)
        bobo.forward(g)
        for j in range(6):
            bobo.pd()
            star(bobo,l,'white')
            bobo.pu()
            bobo.forward(2*g)
        bobo.back(d+g)
    else:
        bobo.left(90)
        for k in range(5):
            bobo.forward(2*g)
            bobo.pd()
            star(bobo, l, 'white')
            bobo.pu()
        bobo.back(d-2*g)
turtle.mainloop()
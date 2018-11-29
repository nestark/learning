import turtle
import math
import cir_example

bobo=turtle.Turtle()
# Draw a blue circle#
bobo.fillcolor("orange")
bobo.begin_fill()
radius=100*math.sin((54/180)*math.pi)/math.sin((36/180)*math.pi)  # Side length of star is 100, calculate the radius
cir_example.circle(bobo, radius)
bobo.end_fill()
# Move the turtle down#
downward=radius*(1-math.cos(72/180*math.pi))
bobo.pu()
bobo.right(90)
bobo.forward(downward)
bobo.left(90)
bobo.forward(radius*math.sin(72/180*math.pi))
bobo.pd()
# Draw a red star#
bobo.fillcolor("red")
bobo.begin_fill()
bobo.right(144)
bobo.forward(100)
bobo.left(72)
bobo.forward(100)
bobo.right(144)
bobo.forward(100)
bobo.left(72)
bobo.forward(100)
bobo.right(144)
bobo.forward(100)
bobo.left(72)
bobo.forward(100)
bobo.right(144)
bobo.forward(100)
bobo.left(72)
bobo.forward(100)
bobo.right(144)
bobo.forward(100)
bobo.left(72)
bobo.forward(100)
bobo.right(72)
bobo.end_fill()
# Keep the draw showing
turtle.mainloop()
from turtle import *

speed("fast")
pencolor('blue')
#hexagon
side = 6
for i in range(side):
    pensize(4)
    fd(100)
    for i in range(side):
        pensize(2)
        fd(50)
        fillcolor('yellow')
        begin_fill()
        for i in range(side):
            pensize(1)
            fd(25)
            dot(10)
            rt(60)
            end_fill()
        rt(60)
    rt(60)
    
hideturtle()
mainloop()
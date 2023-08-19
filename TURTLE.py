import turtle as t
t.pen()
t.bgcolor("black")
colors=["red","green","yellow"]
name=t.textinput("enter your name","enter your name")
s=int(t.numinput("number of sides","how many sides you want",10,1,20))


for i in range(100):
    t.pencolor(colors[i%s%3])
    t.penup()
    t.forward(i*5)
    t.pendown()
    t.write(name,align='left', font=('Arial', 16, 'normal'))
    t.left(360/s+4)

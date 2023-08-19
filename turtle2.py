from turtle import *
color('green', 'yellow')
begin_fill()
while True:
    forward(300)
    left(250)
    if abs(pos()) < 1:
        break
end_fill()
done()
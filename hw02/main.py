import turtle as t
import time

t.speed(10)
t.color("red", "red") #矩形画笔颜色,填充颜色
t.pensize(5) #矩形画笔大小

t.begin_fill()

t.penup()
t.goto(-150, -100) #以(-640, -427)为起点开始绘制
#绘制矩形4条边
t.forward(300) #1
t.left(90)
t.forward(200) #2
t.left(90)
t.forward(300) #3
t.left(90)
t.forward(200) #4
t.left(90)
t.pendown()

t.end_fill()
time.sleep(1)

t.color("yellow", "yellow") #五角星画笔颜色，填充颜色
t.pensize(5) #五角星画笔大小

t.begin_fill()

t.penup()
t.goto(-130, 60) #大五角星
for _ in range(5):
    t.forward(60)
    t.right(144)
t.pendown()

t.end_fill()
time.sleep(1)

t.begin_fill()

t.penup()
t.goto(-58.3, 86.7) #小五角星1
t.right(35)
for _ in range(5):
     t.forward(20)
     t.right(144)
t.pendown()
    
t.end_fill()
time.sleep(1)

t.begin_fill()

t.penup()
t.goto(-34.2, 70) #小五角星2
t.right(13)
for _ in range(5):
     t.forward(20)
     t.right(144)
t.pendown()
    
t.end_fill()
time.sleep(1)
t.begin_fill()

t.penup()
t.goto(-30.5, 40) #小五角星3
t.right(20)
for _ in range(5):
     t.forward(20)
     t.right(144)
t.pendown()
    
t.end_fill()
time.sleep(1)

t.begin_fill()

t.penup()
t.goto(-57, 15.8) #小五角星4
t.left(37)
for _ in range(5):
     t.forward(20)
     t.right(144)
t.pendown()
    
t.end_fill()
time.sleep(1)

t.hideturtle()


















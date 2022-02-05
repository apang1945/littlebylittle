'''
size = input('请输入画笔的粗细:')
a = input('请输入所要画的圆的半径:')
r = float(a)
import turtle
turtle.pensize(size)
turtle.circle(r)
turtle.circle(r * 4)
turtle.circle(r * 8)
turtle.circle(r * 16)


'''
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

'''
import turtle #导入turtle模块

#左上角第一个矩形
turtle.color('red') #画笔改为红色
turtle.goto(50,0) #去坐标（50,0）
turtle.left(90) #箭头左转90度
turtle.forward(50) #前进50像素
turtle.left(90) #箭头左转90度
turtle.forward(50) #前进50像素
turtle.left(90) #箭头左转90度
turtle.forward(50) #前进50像素

#右上角第一个矩形
turtle.left(90) #箭头左转90度
turtle.penup() #抬起画笔
turtle.goto(70,0) #去坐标（70,0）
turtle.pendown() #放下画笔
turtle.forward(50) #前进50像素
turtle.left(90) #箭头左转90度
turtle.forward(50) #前进50像素
turtle.left(90) #箭头左转90度
turtle.forward(50) #前进50像素
turtle.left(90) #箭头左转90度
turtle.forward(50) #前进50像素

#右下角第一个矩形
turtle.penup()
turtle.goto(70,-20)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

#左下角第一个矩形
turtle.penup()
turtle.goto(50,-20)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
'''

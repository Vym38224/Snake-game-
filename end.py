from tkinter import *
from turtle import Turtle, Screen

def start():
    button.destroy()
    button1.destroy()
    import main   

def exit():
    screen._destroy()

turtle = Turtle()
turtle.hideturtle()
screen = Screen()
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.tracer(False)
screen.bgpic("bg.png")
canvas = screen.getcanvas()
button1 = Button(canvas.master, text="EXIT", command=exit, height=2, width=10, background='orange')
button1.pack()
button1.place(x=260, y=299) 

screen.exitonclick()


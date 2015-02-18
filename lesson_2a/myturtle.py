#!/bin/env python

import turtle
import random

colors = ["red", "blue", "yellow", "white", "black", "pink", "orange", "green","lightblue","lightgreen"]

def main(): 
    turtle.setup (width=1000, height=600, startx=0, starty=0)   
    window = turtle.Screen()
    print  window.screensize()
    window.bgcolor("black")
    window.title("My Turtle Screenshot")
    # window.screensize(1024, 768)
    print  window.screensize()

    tea = turtle.Turtle()
    emeo = turtle.Turtle()

    tea.shape("turtle")
    emeo.shape("turtle")    
    tea.speed(10)
    emeo.speed(10)
    tea.penup()
    emeo.penup()
    
    draw_eme(emeo)
    draw_te(tea)
    draw_o(emeo)
    draw_a(tea)
 
    # # Undo all steps
    # while tea.undobufferentries():
    #         tea.undo()
    #         emeo.undo()

    window.exitonclick()

def draw_eme(turtle):
    turtle.color("blue")
    turtle.hideturtle()
    turtle.setpos(-400,-50)
    turtle.left(90)
    turtle.showturtle()
    set_stamp(turtle, 200)
    turtle.right(135)
    set_stamp(turtle, 100)   
    turtle.setpos(-250, -50)
    turtle.left(135)
    set_stamp(turtle, 200)
    turtle.left(135)
    set_stamp(turtle, 80)

def draw_te(turtle):
    turtle.color("grey")
    turtle.setpos(150,-50)
    turtle.left(90)
    set_stamp(turtle, 180)
    turtle.setpos(50, 150)
    turtle.right(90)
    set_stamp(turtle, 180)   

def draw_o(turtle):
    turtle.color("lightblue")
    turtle.setpos(-150, 130)
    for i in range(8):
        turtle.stamp()
        turtle.circle(100, 45)
    
def draw_a(turtle):
    turtle.color("white")
    turtle.setpos(300,-50)
    turtle.left(70)
    set_stamp(turtle, 200)
    turtle.right(135)
    set_stamp(turtle, 180)
    turtle.setpos(330, 50)
    turtle.left(65)
    set_stamp(turtle, 60)


def set_stamp(turtle, length, step=20):
    count = int(length / step)
    for i in range(count):
        turtle.forward(step)
        turtle.stamp()
 



if __name__ == "__main__":
    main()
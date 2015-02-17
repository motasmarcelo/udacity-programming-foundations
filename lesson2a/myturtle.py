#!/bin/env python

import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    window.title("My Turtle Screenshot")

    tur = turtle.Turtle()
    tur2 = turtle.Turtle()

    tur.shape("turtle")
    tur.color("yellow", "white")
    tur.speed(1)
    
    tur2.shape("turtle")
    tur2.color("blue", "black")
    tur2.speed(1)

    tur.up()
    tur.setpos(100,0)
    tur.down()

    tur2.up()
    tur2.setpos(-300,200)
    tur2.down()
    for i in range(4):
        tur.forward(200)        
        tur2.forward(200)
        tur.right(90)
        tur2.right(90)
    
    window.exitonclick()



draw_square()
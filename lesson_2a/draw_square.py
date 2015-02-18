#!/bin/env python

import turtle
import random

colors = ["red", "blue", "yellow", "white", "black", "pink", "green"]

def draw_square():
    window = turtle.Screen()
    window.bgcolor("lightblue")
    window.title("My Turtle Screenshot")

    tur = turtle.Turtle()
    tur2 = turtle.Turtle()

    tur.shape("turtle")
    tur.color("yellow", "white")
    tur.speed(10)
    
    tur2.shape("turtle")
    tur2.color("blue", "black")
    tur2.speed(10)

    tur.up()
    tur.setpos(100,0)
    tur.down()

    tur2.up()
    tur2.setpos(-300,200)
    tur2.down()

    for i in range(3):
        for i in range(4):
            tur.forward(100)
            tur2.forward(200)
            tur.right(90)
            tur2.right(90)
        x,y = tur.position()
        tur.circle(50, 45)
        tur.setpos(x + 10, y)
        tur.color(colors[get_random()], "white")

    

    # # Flower output
    # ninja = turtle.Turtle()
    # ninja.speed(10) 
    # for i in range(180):
    #     ninja.color("black")
    #     ninja.forward(50)
    #     ninja.color("violet")
    #     ninja.forward(50)
    #     ninja.right(30)
    #     ninja.color("yellow")        
    #     ninja.forward(20)
    #     ninja.left(60)
    #     ninja.color("white")        
    #     ninja.forward(50)
    #     ninja.right(30)
        
    #     ninja.penup()
    #     ninja.setposition(0, 0)
    #     ninja.pendown()
        
    #     ninja.right(2)    
    
    # ninja.color("green")
    # ninja .right(90)
    # ninja.pensize(10)
    # ninja.forward(300)
    window.exitonclick()


def get_random():
    return random.randint(1, len(colors) - 1)



draw_square()
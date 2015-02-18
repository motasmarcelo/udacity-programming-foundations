#!/bin/env python

import turtle

def main():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    
    draw_circle(angie, 100)
    
    window.exitonclick()

def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
        
def draw_circle(turtle, radius):
    turtle.circle(radius)


main()
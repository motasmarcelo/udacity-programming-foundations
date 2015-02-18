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
    
    draw_circle(angie)
    
    lisa = turtle.Turtle()
    lisa.shape("triangle")
    lisa.color("green")
    
    draw_triangle(lisa)

    window.exitonclick()

def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
        
def draw_circle(turtle, radius=50):
    turtle.circle(radius)

def draw_triangle(turtle, size=100):
    turtle.right(180)
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)


main()
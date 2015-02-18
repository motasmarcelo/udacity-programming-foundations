#!/bin/env python

import turtle
import random

def main():
    window = turtle.Screen()
    window.bgcolor("red")
    window.colormode(255)

    # brad = turtle.Turtle()
    # brad.shape("turtle")
    # brad.color("yellow")
    # brad.speed(10)
    
    # draw_square(brad)

    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    
    # draw_circle(angie)
    
    lisa = turtle.Turtle()
    lisa.shape("triangle")
    lisa.color("green")
    
    draw_triangle(lisa)

    window.exitonclick()

def draw_square(turtle):
    for i in range(36):
        turtle.right(10)
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
        
def draw_circle(turtle, radius=50):
    turtle.circle(radius)

def draw_triangle(turtle, size=100):
    turtle.speed(10)
    turtle.right(180)
    for i in range(36):
        turtle.right(10)
        turtle.color(*get_random_color())
        if not i % 9:
            turtle.fill(True)
        for i in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.fill(False)


    for i in range(2, 9):
        turtle.color(*get_random_color())
        if i == 2: turtle.fill(True)
        turtle.setpos(0, i*10)
        turtle.circle(i*10)
        turtle.fill(False)
    # turtle.setpos(0, 50)
    # turtle.color(*get_random_color())
    # turtle.circle(50)
    # turtle.setpos(0, 60)
    # turtle.color(*get_random_color())
    # turtle.circle(60)
    turtle.left(90)
    turtle.setpos(0, 0)
    turtle.pensize(10)
    turtle.color("black")
    turtle.forward(200)
    turtle.pensize(1)
    turtle.shape("circle")

def get_random_color():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    return (a,b,c)

main()

"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error                       # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)  
t = turtle.Turtle()                  
t.shape('turtle')                    
t.speed(2)

def circle():
    for i in range(180):
        t.forward(2)
        t.left(2)

def square():
    for i in range(4):
        t.forward(120)
        t.left(90)

def triangle():
    for i in range(3):
        t.forward(130)
        t.left(120)

shape = input("Enter Shape: (Circle, Square, Triangle) ")
if shape == "Circle":
    circle()
elif shape == "Square":
    square()
elif shape == "Triangle":
    triangle()

# TODO)
#   1. Create a turtle. 
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass

turtle.done()
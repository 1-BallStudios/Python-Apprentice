import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

for i in range(5):
    tina.forward(150)                       # Move tina forward by the forward distance
    tina.left(72)                           # Turn tina left by the left turn


turtle.exitonclick()                    # Close the window when we click on it

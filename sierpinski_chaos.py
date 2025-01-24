import turtle
import random

def draw_triangle(vertices, pen):
    #Draw the outline of the main equilateral triangle.
    pen.penup()
    pen.goto(vertices[0]) 
    pen.pendown()
    pen.pensize(2)  
    pen.goto(vertices[1])  
    pen.goto(vertices[2])  
    pen.goto(vertices[0])  
    pen.penup()

def sierpinski_chaos(iterations=10000):
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=600, height=600)
    screen.tracer(1)  # Update the screen after each dot is drawn

    pen = turtle.Turtle()
    pen.speed(100)  # Fastest drawing speed
    pen.penup()
    pen.hideturtle()

    # Define the vertices of an equilateral triangle
    vertices = [(-200, -100), (0, 200), (200, -100)]

    # Draw the outline of the main triangle
    draw_triangle(vertices, pen)

    # Start with a random point inside the triangle
    point = [random.uniform(-200, 200), random.uniform(-100, 200)]

    for _ in range(iterations):
        # Randomly choose one of the three vertices
        vertex = random.choice(vertices)

        # Move halfway from the current point to the chosen vertex
        point[0] = (point[0] + vertex[0]) / 2
        point[1] = (point[1] + vertex[1]) / 2

        # Draw the point
        pen.goto(point[0], point[1])
        pen.dot(2, "black")

        screen.update()

    screen.mainloop()

sierpinski_chaos(iterations=50000)
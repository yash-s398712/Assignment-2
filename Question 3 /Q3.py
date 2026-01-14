import turtle

# Recursive function to draw one edge with inward triangle indentation
def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        segment = length / 3
        draw_edge(segment, depth - 1)
        turtle.left(60)
        draw_edge(segment, depth - 1)
        turtle.right(120)
        draw_edge(segment, depth - 1)
        turtle.left(60)
        draw_edge(segment, depth - 1)

# Function to draw a polygon with recursive edges
def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)

# Main program
def main():
    # User inputs
    sides = int(input("Enter the number of sides (3-6 recommended): "))
    length = int(input("Enter the side length (100-300 recommended): "))
    depth = int(input("Enter the recursion depth (1-3 recommended): "))

    # Setup turtle
    turtle.speed(0)          # Fastest drawing
    turtle.hideturtle()      # Hide the turtle pointer
    turtle.penup()
    
    # Center polygon on screen
    turtle.goto(-length/2, length/2)
    turtle.pendown()

    # Draw the pattern
    draw_polygon(sides, length, depth)

    # Save the output as PostScript file
    ts = turtle.getcanvas()  # get Tkinter canvas
    ts.postscript(file="Q3_output.ps")  # save as .ps file

    # Keep the window open
    turtle.done()

if __name__ == "__main__":
    main()

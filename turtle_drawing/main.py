import turtle
import drawing

def draw_shape(my_turtle, shape):
    ''' 
    This function draws a shape with the Turtle.
    This should be rewritten as a method in the Shape class for this scenario.
    '''
    # TODO: This function should be written to be a method in the Shape class
        
    points = shape['points'] # gets list of points to draw
    # Put the pen up, so the turtle isn't drawing on the canvas and move to first point
    my_turtle.penup()
    my_turtle.goto(points[0])

    # Sets up colour for shape fill colour and puts pen down
    my_turtle.color(shape['colour'])
    my_turtle.begin_fill()
    my_turtle.pendown()

    # Moves around to different points to draw the shape
    for point in points:
        my_turtle.goto(point)
    
    # Moves to first point, to close the shape
    my_turtle.goto(points[0])
    my_turtle.end_fill()

'''
    The mainline of the drawing program starts here
'''

# A list of shapes, which we'll loop through later in the program to draw our shapes
shapes = []
# Creates an instance of a turtle which will be used for drawing the shapes
my_turtle = turtle.Turtle()

b_triangle_points = [drawing.Point(-120, 200),drawing.Point(-20, 200), drawing.Point(-70, 100)]
blue_triangle = [drawing.Shape('blue', b_triangle_points, my_turtle)
shapes.append(blue_triangle)

square = [drawing.Point(-200, -100), drawing.Point(-200, -150), drawing.Point(-150, -150), drawing.Point(-150, -100)]
orange_square = drawing.Shape('orange', square, my_turtle)
shapes.append(orange_square)

r_triangle_points = [drawing.Point(100, 200),drawing.Point(250, 200), drawing.Point(175, 50)]
blue_triangle = [drawing.Shape('red', r_triangle_points, my_turtle)
rt_points = [(100, 200), (250, 200), (175, 50)]
shapes.append(red_triangle)

# Draws all of the shapes that are in the list in the window
for shape in shapes:
    # TODO: Modify the next line to use the draw method on the Shape object
    shape.draw()
    
# This line will mean that the Turtle window won't close until we click
turtle.Screen().exitonclick() 
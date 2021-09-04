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

# Creates a dictionary for a blue triangle shape
# TODO: Change this code to create a list of Point objects and a Shape object, rather than a dictionary

blue_triangle = ['Point','Shape']
blue_triangle['colour'] = 'blue'
bt_points = [(-120, 200), (-20, 200), (-70, 100)]
blue_triangle['points'] = bt_points
# Adds the blue triangle to the list of shapes
shapes.append(blue_triangle)

# Creates a dictionary for an orange square shape
# TODO: Change this code to create a list of Point objects and a Shape object, rather than a dictionary
orange_square = ['Point','Shape']
orange_square['colour'] = 'orange'
os_points = [(-200, -100), (-200, -150), (-150, -150), (-150, -100)]
orange_square['points'] = os_points
# Adds the orange square to the list of shapes
shapes.append(orange_square)

# Creates a dictionary for a red triangle shape
# TODO: Change this code to create a list of Point objects and a Shape object, rather than a dictionary
red_triangle = ['Point','Shape']
red_triangle['colour'] = 'red'
rt_points = [(100, 200), (250, 200), (175, 50)]
red_triangle['points'] = rt_points
# Adds the blue triangle to the list of shapes
shapes.append(red_triangle)

# Draws all of the shapes that are in the list in the window
for shape in shapes:
    # TODO: Modify the next line to use the draw method on the Shape object
    draw_shape(my_turtle, ['Shape'])
    
# This line will mean that the Turtle window won't close until we click
turtle.Screen().exitonclick() 
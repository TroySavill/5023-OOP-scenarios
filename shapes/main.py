import shapes
import math

def create_rectangle():
    ''' 
    Function that prompts user for rectangle length and width,
    calculates the area and perimeter for the rectangle and 
    prints these out (We assume that the lengths and widths will be floats)
    '''
    # Prompts the user for a length and width for the rectangle
    print()
    length = float(input('Rectangle length: '))
    width = float(input('Rectangle width: '))


    # TODO: Should be replaced with the creation of a Rectangle object
    rectangle = shapes.Rectangle(length, width)

    # Calculates the area for the rectangle and prints this rounded to 2 decimal places
    # TODO: Replace the next line with a call to the Rectangle's calculate_area() method
    area = rectangle.calculate_area()
    print(f'Rectangle area: {round(area, 2)}')
    print()
    # Calculates the perimeter for the rectangle and prints this rounded to 2 decimal places
    # TODO: Replace the next line with a call to the Rectangle's calculate_perimeter() method
    perimeter = rectangle.calculate_perimeter()
    print(f'Rectangle perimeter: {round(perimeter, 2)}')
    print()

def create_circle():
    ''' 
    Function that prompts user for the circle radius,
    calculates the area and circumference for the circle and 
    prints these out (We assume that the input will be a float)
    '''
    # Prompts the user for a radius for the circle
    print()
    radius = float(input('Circle radius: '))

    # TODO: Should be replaced with the creation of a Circle object
    circle = shapes.Circle(radius)

    # Calculates the area for the circle and prints this rounded to 2 decimal places
    # TODO: Replace the next line with a call to the Circle's calculate_area() method
    area = circle.calculate_area() 
    print(f'Circle area: {round(area,2)}')

    # Calclates the circumference for the circle and prints this rounded to 2 decimal places
    # TODO: Replace the next line with a call to the Circle's calculate_circumference() method
    circumference = circle.calculate_circumference()
    print(f'Circle circumference: {round(circumference, 2)}')
    print()

def show_menu():
    ''' Utility function to show the menu options '''
    print('---\nMenu for shapes program, select an option:')
    print('1 - Create a rectangle.')
    print('2 - Create a circle.')
    print('0 - Stop the program.')
    print('---')
    selection = input('Selection: ')
    if selection == '1' or selection == '2':
        if selection == '1':
            create_rectangle()
            show_menu()
        elif selection == '2':
            create_circle()
            show_menu()

# Mainline of the program
show_menu()
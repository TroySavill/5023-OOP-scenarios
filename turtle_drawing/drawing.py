class Shape:
    def __init__(self, colour:str, points:list, my_turtle):
        self.colour = colour
        self.points = points
        self.my_turtle = my_turtle
    
    def draw(self):  
        self.my_turtle.penup()
        self.my_turtle.goto((self.points[0].x,self.points[0].y))
        self.my_turtle.color(self.colour)
        self.my_turtle.begin_fill()
        self.my_turtle.pendown()

        for point in self.points:
            self.my_turtle.goto((point.x,point.y))
        self.my_turtle.goto((self.points[0].x,self.points[0].y))
        self.my_turtle.end_fill()
class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y   
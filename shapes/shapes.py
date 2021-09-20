import math

class Rectangle:
    def __init__(self, length:float, width:float):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return (self.length*2) + (self.width*2)

class Circle:
    def __init__(self, radius:float):
        self.radius = radius
    
    def calculate_area(self):
        return (self.radius*self.radius)*math.pi

    def calculate_circumference(self):
        return 2* self.radius*math.pi

# Create a class called Student
class Student:
  
    def __init__(self, name: str, english_mark: int, science_mark: int, mathematics_mark: int, completed_assessments: bool,):
        self.name = name
        self.english_mark = english_mark
        self.science_mark = science_mark
        self.mathematics_mark = mathematics_mark
        self.completed_assessments = completed_assessments
    
    def average_mark(self):
        return round((self.english_mark + self.science_mark + self.mathematics_mark) / 3)
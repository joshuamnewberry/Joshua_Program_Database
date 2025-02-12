class NonPositiveNumberError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Not a positive number"

class NoGradeError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "You lose, no grades"

class Student:
    def __init__(self, name:int = "", grades:list = []) -> None:
        self.name = name
        self.grades = grades
    
    def add_grade(self, grade:float) -> None:   
        if grade < 0:
            raise NonPositiveNumberError
        if type(grade) != float and type(grade) != int:
            raise TypeError
        self.grades.append(float(grade))
    
    def calculate_average(self) -> float:
        if len(self.grades) == 0:
            raise NoGradeError
        return sum(self.grades) / len(self.grades)
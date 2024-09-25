from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, ):
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass

class Square(Shape):
    def __init___(self, length:float) -> None:
        self.length = length
        super()
    
    def get_length(self) -> float:
        return self.length
    
    def set_length(self, length:float) -> None:
        self.length = length

    def get_area(self) -> float:
        return pow(self.length, 2)

class Circle(Shape):
    def __init__(self, radius:float) -> None:
        self.radius = radius
        super()
    
    def get_radius(self) -> float:
        return self.radius
    
    def set_radius(self, radius:float) -> None:
        self.radius = radius
    
    def get_area(self) -> float:
        return pow(self.radius, 2) * math.pi
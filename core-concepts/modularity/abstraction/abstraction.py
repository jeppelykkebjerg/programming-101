from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage
shapes: list = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # Outputs: 78.5 for Circle, 24 for Rectangle
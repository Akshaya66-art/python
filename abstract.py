from abc import ABC
class Shape(ABC):
    def area(self):
        print("area of the shape")
    def peremeter(self):
        print("peremeter of the shape")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        def area(self):
            return 3.148*self.radius*self.radius
        def peremeter(self):
            return 2*3.14*self.radius
class Square(Shape):
    def __init__(self,side_length):
        self.side_length=side_length
    def area(self):
        return self.side_length*self.side_length
    def peremeter(self):
        return 4*self.side_length
c=Circle(5)
s=Square(6)
print(f"the area of circle:{c.area()}")
print(f"the peremeter of circle:{c.peremeter()}")
print(f"the area of square:{s.area()}")
print(f"the peremeter of square:{s.peremeter()}")

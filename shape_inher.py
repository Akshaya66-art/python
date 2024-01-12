class Shape:
    def __init__(self,area):
        self.area=area
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        result=(3.14)*self.radius*self.radius
        print(f'Area of circle:{result}')
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        result=self.length*self.breadth*(0.5)
        print(f'Area of Rectangle:{result}')
c = Circle(2)
r = Rectangle(2,4)
c.area()
r.area()
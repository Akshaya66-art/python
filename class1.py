class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"my name is:{self.name}my age is:{self.age}")
p1=Person("manu",5)
p1.display()
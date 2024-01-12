class Person:
    def __init__(self):#non-parameter
        print("welcome")

    def display(self,name,age):
        self.name=name
        self.age=age
        print(f"my name is:{self.name}my age is:{self.age}")
p1=Person()
p1.display("anu",25)
class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print(f"employee name:{self.name}\nid:{self.id}\nsalary{self.salary}")
p1=employee("meha",123,50000)
p1.display()
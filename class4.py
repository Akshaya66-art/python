class student:
    def __init__(self,name,number,address):
        self.name=name
        self.number=number
        self.address=address
    def display(self):
        print(f"student name is:{self.name}\nstudent number is:{self.number}\nstudent address is:{self.address}")
p1=student("neha",97681772,"kochi,edappilly")
p1.display()
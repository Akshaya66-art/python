class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("welcome to animals world")
class dog(Animal):
    def speak(self):
        print(f"{self.name}says bowwww!!!!")
class cat(Animal):
    def speak(self):
        print(f"{self.name}says meoww!!!!")
d=dog("puppy")
d.speak()
c=cat("cia")
c.speak()

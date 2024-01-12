class Animal:
    def speak(self):
        print("Anoimal speaking")
class dog(Animal):
    def bark(self):
        print("dog is barking")
class dogchild(dog):
    def eat(self):
        print("dogchild is eating")
d=dogchild()
d.bark()
d.eat()
d.speak()
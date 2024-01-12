class Calculation1:
    def summation(self,a,b):
        return a+b
class Calcutaion2:
    def multiplication(self,a,b):
        return a*b
class Calculation3(Calculation1,Calcutaion2):
    def Divide(self,a,b):
        return a/b
d=Calculation3()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.Divide(10,20))
class Bank:
    def getroi(self):
        return 10;
class SBI(Bank):
    def getroi(self):
        return 7;
class ICICI(Bank):
    def getroi(self):
        return 8;
b1=Bank()
b2=SBI()
b3=ICICI()
print("bank rate of interst:",b1.getroi())
print("bank rate of interest:",b2.getroi())
print("icici rate of interest:",b3.getroi())

class Arithmetic:
    def __init__(self,no1,no2):
        Arithmetic.Value1 = no1
        Arithmetic.Value2 = no2

    def Accept(self):
        self.Value1 = int(input("Enter the Value1 : "))
        self.Value2 = int(input("Enter the Value2 : "))

    def Addition(self):
        self.Add = self.Value1 + self.Value2
        print("Addition is : ",self.Add)
    
    def Substraction(self):
        self.Sub = self.Value1 - self.Value2
        print("Substrction is : ",self.Sub)
    
    def Multiplication(self):
        self.Mult = self.Value1 * self.Value2
        print("Multiplication is : ",self.Mult)
        
    def Division(self):
        self.Div = self.Value1 / self.Value2
        print("Division is : ",self.Div)

aobj = Arithmetic(0,0)

aobj.Accept()
aobj.Addition()
aobj.Substraction()
aobj.Multiplication()
aobj.Division()
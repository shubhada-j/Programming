class Numbers:
    Value = 0

    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):

        if self.Value <= 1:
            return False
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        self.Sum = 0

        for i in range(1,self.Value):

            if self.Value % i == 0:
                self.Sum = self.Sum + i
    
        
        if self.Sum == self.Value:
            return True
        else:
            return False
        
    def Factors(self):

        for i in range(1,self.Value):
            if self.Value % i == 0:
                print("Factors are : ",i)

        print("\n")

    def SumFactors(self):
        self.SumFact = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                self.SumFact = self.SumFact + i
    
        return self.SumFact
    

obj1 = Numbers(10)

print("Prime : ",obj1.ChkPrime())
print("Perfect : ",obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors : ",obj1.SumFactors())
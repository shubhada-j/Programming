# Write a program which accept one number from user and return its addition of its Factors

def FactorsSum(No):
    Fact = 0
    
    for i in range(1,No):
        if(No % i == 0):
            Fact = Fact + i
    return Fact

def main():
    Value = int(input("Enter the number : "))
    
    Ret = FactorsSum(Value)
    print("Factors Sum is : ",Ret)

if __name__ == "__main__":
    main()
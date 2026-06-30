# Write a program which accepts two numbers and 
# prints addition, substraction, multiplication and division

def Addition(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def Substraction(Value1, Value2):
    Ans = Value1 - Value2
    return Ans

def Multiplication(Value1, Value2):
    Ans = Value1 * Value2
    return Ans

def Division(Value1, Value2):
    Ans = Value1/Value2
    return Ans
          
def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Addition(No1,No2)
    print("Addition is : ",Ret)

    Ret = Substraction(No1,No2)
    print("Substraction is : ",Ret)

    Ret = Multiplication(No1,No2)
    print("Multiplication is : ",Ret)

    Ret = Division(No1,No2)
    print("Division is : ",Ret)
    
if __name__ ==  "__main__":
    main()

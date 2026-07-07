import Arithmetic

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Arithmetic.Add(Value1, Value2)
    print("Addition is : ",Ret)
    
    Ret = Arithmetic.Sub(Value1, Value2)
    print("Substraction is : ",Ret)

    Ret = Arithmetic.Mult(Value1, Value2)
    print("Multiplication is : ",Ret)

    Ret = Arithmetic.Div(Value1, Value2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()
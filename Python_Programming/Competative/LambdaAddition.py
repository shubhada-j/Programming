# Write a lambda function which accepts two number and returns addition of that numbers.

Addition = lambda No1, No2 : No1 + No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Addition(Value1,Value2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()
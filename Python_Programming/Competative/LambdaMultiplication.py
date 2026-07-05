# Write a lambda function which accepts two numbers and returns multiplication of that number.

Multiplication = lambda No1, No2 : No1 * No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Multiplication(Value1,Value2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()
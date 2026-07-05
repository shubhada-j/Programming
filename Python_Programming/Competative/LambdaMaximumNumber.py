# Write a lambda function which accepts three number and returns maximum number.

Maximum = lambda No1, No2, No3 : max(No1, No2, No3)

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
    Value3 = int(input("Enter the third number : "))

    Ret = Maximum(Value1,Value2,Value3)

    print("Maximum number is : ",Ret)
    
if __name__ == "__main__":
    main()
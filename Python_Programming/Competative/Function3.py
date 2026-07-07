# Write a program which contains one function named as Add() which accept two numbers from user and return addition of that two numbers.

def Add(Number1,Number2):
    Ans = Number1 + Number2
    return Ans

def main():
    Value1 = int(input("Enter number : "))
    Value2 = int(input("Enter number : "))

    Ret = Add(Value1,Value2)
    print("Addition of two numbers are : ",Ret)
    
if __name__ == "__main__":
    main()
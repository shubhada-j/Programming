# Write a program which accepts one number and prints factorial of that number

def Factorial(Value):
    Ans = 0
    for i in range(1,Value+1):
        Ans = Ans + i
    return Ans

def main():
    No = int(input("Enter number : "))

    Ret = Factorial(No)
    print("Factorial of",No,"is : ",Ret)

if __name__ ==  "__main__":
    main()

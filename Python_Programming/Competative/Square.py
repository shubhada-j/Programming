# Write a program which accepts one number and prints square of that number

def SquareOfNumber(Value):
    Ans = Value * Value

    return Ans

def main():
    No = int(input("Enter number :"))

    Ret = SquareOfNumber(No)
    print("Square of", No,"is :", Ret)

if __name__ ==  "__main__":
    main()

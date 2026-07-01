# Write a program which accepts one number and prints cube of that number

def CubeOfNumber(Value):
    Ans = Value * Value * Value

    return Ans

def main():
    No = int(input("Enter number :"))

    Ret = CubeOfNumber(No)
    print("Cube of", No,"is :", Ret)

if __name__ ==  "__main__":
    main()

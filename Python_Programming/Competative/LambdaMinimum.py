# Write a lambda function which accepts two numbers and returns minimum number.

Minimum = lambda No1, No2 : No1 > No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Minimum(Value1,Value2)

    if(Ret == True):
        print(Value2,"is Minimum")
    else:
        print(Value1,"is Minimum")

if __name__ == "__main__":
    main()
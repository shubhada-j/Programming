# Write a lambda function which accepts one number and returns True if that number is divisible by 5.

Even = lambda No : No % 5 == 0

def main():
    Value = int(input("Enter the number : "))

    Ret = Even(Value)

    if(Ret == True):
        print("Number is Divisible by 5")
    else:
        print("Number is not Divisible by 5")

if __name__ == "__main__":
    main()
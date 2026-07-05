# Write a lambda function which accepts one number and returns true if that number is Odd.

Even = lambda No : No % 2 != 0

def main():
    Value = int(input("Enter the number : "))

    Ret = Even(Value)

    if(Ret == True):
        print("Number is Odd")
    else:
        print("Number is Even")

if __name__ == "__main__":
    main()
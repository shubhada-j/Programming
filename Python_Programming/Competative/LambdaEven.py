# Write a lambda function which accepts one number and returns True if that number is Even.

Even = lambda No : No % 2 == 0

def main():
    Value = int(input("Enter the number : "))

    Ret = Even(Value)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()
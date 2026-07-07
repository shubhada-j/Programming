# Write a program which accept number from user and check wheather that number is positive or negative or zero

def Check(No):
    if(No > 0):
        print("Number is Positive")
    elif(No < 0):
        print("Number is Negative")
    else:
        print("Number is Zero")

def main():
    Value = int(input("Enter number : "))

    Check(Value)
    
if __name__ == "__main__":
    main()
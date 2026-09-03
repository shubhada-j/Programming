CheckEven = lambda No: (No % 2 == 0)

def main():
    Value = int(input("Enter the number : "))
    
    Ret = CheckEven(Value)

    if Ret == True:
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()


# == , != , < , > , <= , >= returns --> True/False, Yes/No, 1/0

# Write a program which accepts one number and prints multiplication table of that number

def TableOfNumber(Value):
    for no in range(1,11):
        Ans = Value * (no)
        print(Ans)

def main():
    No = int(input("Enter number : "))

    TableOfNumber(No)

if __name__ ==  "__main__":
    main()

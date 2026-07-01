# Write a program which accepts one number and prints sum of first N natural numbers

def SumOfN(Value):
    Ans = 0
    for no in range(1,Value+1):
        Ans = Ans + no
     
    print(Ans)

def main():
    No = int(input("Enter number : "))

    SumOfN(No)

if __name__ ==  "__main__":
    main()

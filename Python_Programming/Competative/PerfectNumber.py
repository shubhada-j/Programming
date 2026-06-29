#Write a program which Accept one number and checks whether it is perfect or not

def PerfectNumber(Value):
    Sum = 0

    for i in range(1,Value):
        if(Value % i == 0):
            Sum = Sum + i
    return Sum
            
def main():
    No = int(input("Enter number : "))
    temp = No

    Ret = PerfectNumber(No)

    if(Ret == temp):
        print(No,"is Perfect Number")
    else:
        print(No,"is not Perfect Number")


if __name__ ==  "__main__":
    main()

# Write a program which accepts one number and checks whether it is prime or not

def PrimeNumber(Value):
    for i in range(2,Value+1):
        if(Value % i != 0):
            return True
        else:
            return False
            
def main():
    No = int(input("Enter number : "))

    Ret = PrimeNumber(No)

    if(Ret == True):
        print(No,"is Prime Number")
    else:
        print(No,"is not Prime Number")


if __name__ ==  "__main__":
    main()

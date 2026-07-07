# Write a program which accept one number from user and check whether number is prime or not

def PrimeNumber(No):
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True
        
def main():
    Value = int(input("Enter number : "))

    Ret = PrimeNumber(Value)
    if(Ret == True):
        print("It is Prime")
    else:
        print("It is not Prime")

if __name__ == "__main__":
    main()
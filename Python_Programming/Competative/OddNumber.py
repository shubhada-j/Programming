#Write a program which accepts one number and prints all odd numbers till that number

def OddNumber(Value):
    for i in range(1,Value+1):
        if(i % 2 != 0):
            print(i)

def main():
    No = int(input("Enter number : "))

    OddNumber(No)

if __name__ ==  "__main__":
    main()

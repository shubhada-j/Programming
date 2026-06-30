# Write a program which accepts one number and 
# prints that many numbers starting from 1

def Numbers(Value):
    for i in range(1,Value+1):
        print(i)

def main():
    No = int(input("Enter number : "))

    Numbers(No)

if __name__ ==  "__main__":
    main()

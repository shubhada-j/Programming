# Write a program which accepts one number and 
# prints that many numbers in reverse order

def Numbers(Value):
    for i in range(Value,0,-1):
        print(i)

def main():
    No = int(input("Enter number : "))

    Numbers(No)

if __name__ ==  "__main__":
    main()

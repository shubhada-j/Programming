# Write a program which accepts one number and prints all even numbers till that number

def EvenNumber(Value):
    for i in range(1,Value+1):
        if(i % 2 == 0):
            print(i)

def main():
    No = int(input("Enter number : "))

    EvenNumber(No)

if __name__ ==  "__main__":
    main()

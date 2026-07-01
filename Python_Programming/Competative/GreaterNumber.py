# Write a program which contains one function ChkGreater() that accepts two numbers 
# and print the greater number

def ChkGreater(Value1,Value2):
    if(Value1 > Value2):
        print(Value1,"is greater")
    else:
        print(Value2,"is greater")


def main():
    No1 = int(input("Enter the first number :"))
    No2 = int(input("Enter the second number :"))

    ChkGreater(No1,No2)

if __name__ ==  "__main__":
    main()

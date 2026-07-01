# Write a program which accepts one number and prints reverse of that number

def ReverseNumber(Value):
    
    while(Value != 0):
        Digit = Value % 10
        print(Digit, end = "")
        Value = Value//10    
            
def main():
    No = int(input("Enter number : "))

    ReverseNumber(No)
    
if __name__ ==  "__main__":
    main()

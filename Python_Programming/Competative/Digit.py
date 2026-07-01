# Write a program which accepts one number and prints count of digits in that number

def CountDigit(Value):
    Digit = 0

    while(Value != 0):
        Digit = Digit + 1
        Value = Value//10
    
    return Digit
        
            
def main():
    No = int(input("Enter number : "))

    Ret = CountDigit(No)
    
    print("Number of Digits : ",Ret)

if __name__ ==  "__main__":
    main()

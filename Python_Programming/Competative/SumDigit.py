# Write a program which accepts one number and prints sum of digits

def SumDigit(Value):
    Sum = 0

    while(Value != 0):
        Digit = Value % 10
        Sum = Sum + Digit
        Value = Value//10

    return Sum
        
            
def main():
    No = int(input("Enter number : "))

    Ret = SumDigit(No)
    
    print("Sum of Digits : ",Ret)

if __name__ ==  "__main__":
    main()

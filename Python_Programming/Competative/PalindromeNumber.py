# Write a program which accepts one number and checks whether it is palindrome or not

def PalindromeNumber(Value):
    temp = Value
    reverse = 0
    while(Value != 0):
        Digit = Value % 10
        reverse = (reverse * 10) + Digit
        Value = Value//10    

    if(reverse == temp):
        return True
    
          
def main():
    No = int(input("Enter number : "))

    Ret = PalindromeNumber(No)

    if(Ret == True):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")
    
if __name__ ==  "__main__":
    main()

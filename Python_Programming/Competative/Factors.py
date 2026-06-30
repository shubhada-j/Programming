# Write a program which accept one number and prints its factors

def Factors(Value):
    for i in range(1,Value+1):
        if(Value % i == 0):
            print(i)
          
def main():
    No = int(input("Enter number : "))

    Ret = Factors(No)
    
if __name__ ==  "__main__":
    main()

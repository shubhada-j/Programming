# Write a program which accepts one number and checks whether it is divisible by 3 and 5

def Divisible(Value):
    if((Value % 3 == 0) & (Value % 5 == 0)):
        return True 
    else:
        return False
        
def main():
    No = int(input("Enter number : "))

    Ret = Divisible(No)

    if(Ret == True):
        print(No,"is divisible by 3 and 5")
    else:
        print(No,"is not divisible by 3 and 5")
   
if __name__ ==  "__main__":
    main()

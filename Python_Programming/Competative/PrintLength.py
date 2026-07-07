# Write a program which accept name from user and display length of its name

def Display(Value):
    Ans = len(Value)
    return Ans

def main():
    Name = str(input("Enter the name : "))

    Ret = Display(Name)

    print("Length is : ",Ret)
    
if __name__ == "__main__":
    main()
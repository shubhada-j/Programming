#Write a program which accepts a file name and one string from the user and returns the freequency of that string in the file

def CountFrequency(First,Data):
    fobj = open(First,"r")
    print("File opened")
    FData = fobj.read()
    
    Words = FData.split()

    Count = 0

    for word in Words:
        if(word == Data):
            Count += 1
    
    return Count

def main():
    Ret = 0

    FName = input("Enter the file name : ")

    Value = input("Enter the string : ")

    Ret = CountFrequency(FName,Value)

    print("Count of String is : ",Ret)

if __name__ == "__main__":
    main()
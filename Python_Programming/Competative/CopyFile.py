# Write a program which accepts two file names from the user


def Copy(First,Second):
    fobj1 = open(First,"r")
    print("First File gets opened")
    Data = fobj1.read()
    
    fobj2  = open(Second,"w")
    print("Second File gets opened")
    
    fobj2.write(Data)
    print("New File created amd Data Copied" \
    "")

    fobj2.close()
    fobj1.close()

def main():
    FName = input("Enter file name : ")
    SName = input("Enter file name : ")
    
    Copy(FName,SName)

if __name__ == "__main__":
    main()
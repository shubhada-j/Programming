# Write a program which accepts a file name from user and counts how many lines are present in the file

def Count(File):
    iCount = 0
    try:
        fobj = open(File,"r")
        for line in fobj:
            iCount += 1

        fobj.close()

        return iCount

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
        return 0

def main():
    Name = input("Enter file name : ")

    Ret = Count(Name)

    if(Ret != 0):
        print("Number of lines are : ",Ret)
    else:
        print("File is empty")

if __name__ == "__main__":
    main()
# Write a program which accepts a file name from user and counts how many words are present in the file

def Count(File,Value):
    icount = 0
    try:
        fobj = open(File,"r")
        
        for line in fobj:
            words = line.split()

            for word in words:
                if(Value == word):
                    return True

        fobj.close()
        
        return False

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
        return False

def main():
    Ret = False
    Name = input("Enter file name : ")
    Data = input("Enter the word : ")

    Ret = Count(Name,Data)
    if(Ret == True):
        print("Word is Found")
    else:
        print("Word is not found")

if __name__ == "__main__":
    main()
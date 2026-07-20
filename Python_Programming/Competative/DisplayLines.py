# Write a program which accepts a file name from user and counts how many lines are present in the file

def Count(File):
    iCount = 0
    try:
        fobj = open(File,"r")

        for line in fobj:
            print(line)

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

def main():
    Name = input("Enter file name : ")

    Count(Name)

if __name__ == "__main__":
    main()
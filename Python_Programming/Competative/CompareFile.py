# Write a program which accepts two files name through command line arguments and compare the both files

import sys

def CompareFile(First,Second):
    fobj1 = open(First,"r")
    print(f"{First} File gets opened")
    
    Data1 = fobj1.read()

    fobj2 = open(Second,"r")
    print(f"{Second} File gets opened")

    Data2 = fobj2.read()

    if(Data1 == Data2):
        print("Success")
    else:
        print("Failure")

    fobj1.close()
    fobj2.close()

def main():
    if(len(sys.argv) == 3):
        CompareFile(sys.argv[1],sys.argv[2])
    else:
        print("Invalid Data")

if __name__ == "__main__":
    main()
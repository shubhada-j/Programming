# Write a program which accept an existing file name through command line arguments, 
# creates a new file named Demo.txt and copies all contents from the given file into Demo.txt
import sys

def CopyFile(First):
    fobj1 = open(First,"r")
    print(f"{First} File gets opened")
    
    Data = fobj1.read()

    fobj2 = open("Demo.txt","w")
    print("File gets opened")

    fobj2.write(Data)
    print("file copied data")

    fobj1.close()
    fobj2.close()

def main():
    if(len(sys.argv) == 2):
        CopyFile(sys.argv[1])
    else:
        print("Invalid Data")

if __name__ == "__main__":
    main()
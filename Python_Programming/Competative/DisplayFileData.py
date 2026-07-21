#Write a program which accept a file name from the user 
#opens that file and display the entire contents on the console

import os 

def Check(Name):
    fobj = open(Name,"r")
    print("File gets opened")

    Data = fobj.read()

    print(Data)

    fobj.close()

def main():
    Value = input("Enter file name : ")

    Check(Value)
    
if __name__ == "__main__":
    main()
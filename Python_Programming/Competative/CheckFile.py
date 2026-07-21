# Write a program which accepts a file name from the user and 
# checks whether that file exists in the current directory or not

import os 

def Check(Name):
    if((os.path.exists(Name))):
        return True
    else:
        return False

def main():
    Value = input("Enter file name : ")

    Ret = Check(Value)   

    if(Ret == True):
        print("File exists")
    else:
        print("File is not exists")

if __name__ == "__main__":
    main()
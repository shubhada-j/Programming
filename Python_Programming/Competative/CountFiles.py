import os 


def CountFile():
    Count = 0
    
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        for fname in FileName:
            Count += 1 

    return Count
    
def main():
    Ret = 0

    Ret = CountFile()
    print("The number of Files are : ",Ret)

if __name__ == "__main__":
    main()
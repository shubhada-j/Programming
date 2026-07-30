//Write a program which accepts file name from user and display size of file

#include<stdio.h>
#include<fcntl.h>

int DisplaySize(char FName[])
{
    int fd = 0;
    int iValue = 0;
    int iSize = 0;
    char Arr[100] = {'\0'};

    fd = open(FName,O_RDONLY);

    if(fd == -1)
    {
        printf("Unable to open file\n");
        return -1;
    }
    
    else
    {
        printf("File gets open successfully\n");

        while((iValue = read(fd,Arr,sizeof(Arr))) != 0)
        {
            iSize = iSize + iValue;
        }

        return iSize;

        close(fd);
    }
}

int main()
{
    char FileName[30];
    int iRet = 0;

    printf("Enter file name : ");
    scanf("%s",FileName);

    iRet = DisplaySize(FileName);
    printf("Size of File is : %d",iRet);

    return 0;
}
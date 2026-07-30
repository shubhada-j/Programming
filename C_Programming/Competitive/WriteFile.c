//Write a program which accepts file name from user and one string from user Write that string at the end of file

#include<stdio.h>
#include<string.h>
#include<fcntl.h>

void Display(char FName[], char cString[])
{
    int fd = 0;
    int iValue = 0;
    int iSize = 0;
    char Arr[100] = {'\0'};

    fd = open(FName,O_RDWR | O_APPEND);

    if(fd == -1)
    {
        printf("Unable to open file\n");
    }
    
    else
    {
        printf("File gets open successfully\n");

        iValue = write(fd,cString,strlen(cString));

        close(fd);
    }
}

int main()
{
    char FileName[30];
    int iRet = 0;
    char Data[100];

    printf("Enter file name : ");
    scanf("%s",FileName);

    printf("Enter the string : ");
    scanf("%s",Data);

    Display(FileName,Data);
    
    return 0;
}
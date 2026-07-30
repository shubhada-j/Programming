//Write a program which accepts file name from user and one count from user and read that number of characters from starting position.

#include<stdio.h>
#include<stdlib.h>
#include<io.h>
#include<fcntl.h>

void DisplayN(char FName[], int iSize)
{
    int fd = 0;
    int iValue = 0;
    char Arr[100] = {'\0'};

    fd = open(FName,O_RDONLY);

    if(fd == -1)
    {
        printf("Unable to open file\n");
    }
    
    else
    {
        printf("File gets open successfully\n");
        
        iValue = read(fd,Arr,iSize);

        printf("%s",Arr);

        close(fd);
    }
}

int main()
{
    char FileName[30];
    int iValue = 0;

    printf("Enter file name : ");
    scanf("%s",FileName);

    printf("Enter the number of characters : ");
    scanf("%d",&iValue);

    DisplayN(FileName,iValue);
    

    return 0;
}
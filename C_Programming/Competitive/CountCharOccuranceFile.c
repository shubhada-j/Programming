//Write a program which accepts file name and one character from user and count number of occurrences of that character from that file.

#include<stdio.h>
#include<stdlib.h>
#include<io.h>
#include<fcntl.h>

int CountChar(char FName[],char Ch)
{
    int fd = 0;
    int Frequency = 0;
    int iValue = 0;
    int i = 0;
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
        
        while((iValue = read(fd,Arr,sizeof(Arr))) > 0)
        {
            for(i = 0; i < iValue; i++)
            {
                if(Arr[i] == Ch)
                {
                    Frequency++;
                }
            }
        }

        close(fd);

        return Frequency; 
    } 
}

int main()
{
    char FileName[30];
    int iRet = 0;
    char cValue = '\0';

    printf("Enter file name : ");
    scanf("%s",FileName);

    printf("Enter the character : ");
    scanf(" %c",&cValue);

    iRet = CountChar(FileName,cValue);
    printf("Frequency is : %d",iRet);

    return 0;
}
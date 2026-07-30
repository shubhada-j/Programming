//Write a program which accepts file name from user and count number of white spaces from that file.

#include<stdio.h>
#include<stdlib.h>
#include<io.h>
#include<fcntl.h>

int CountSmall(char FName[])
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
                if(Arr[i] == ' ')
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

    printf("Enter file name : ");
    scanf("%s",FileName);

    iRet = CountSmall(FileName);
    printf("Number of White spaces are : %d",iRet);

    return 0;
}
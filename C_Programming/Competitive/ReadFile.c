//Write a program which accepts file name from user and read all data from that file and display contents on screen

#include<stdio.h>
#include<fcntl.h>

void Display(char FName[])
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
        
        iValue = read(fd,Arr,sizeof(Arr));

        printf("%s",Arr);

        close(fd);
    }
}

int main()
{
    char FileName[30];

    printf("Enter file name : ");
    scanf("%s",FileName);

    Display(FileName);
    

    return 0;
}
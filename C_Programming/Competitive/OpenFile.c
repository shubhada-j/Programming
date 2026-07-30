//Write application which accept file name from user and open that file in read mode

#include<stdio.h>
#include<fcntl.h>

void OpenFile(char FName[])
{
    int fd = 0;

    fd = open(FName,O_RDONLY);

    if(fd == -1)
    {
        printf("Unable to open file");
    }
    else
    {
        printf("File gets open successfully");
    }
}

int main()
{
    char FileName[30];

    printf("Enter file name : ");
    scanf("%s",FileName);

    OpenFile(FileName);

    return 0;
}
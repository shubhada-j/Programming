//Write a program which accept string from user and count number of white spaces.

#include<stdio.h>

void CountSpace(char *str)
{
    int iCount = 0;

    while(*str != '\0')
    {
        if(*str == ' ')
        {
           iCount++;
        }
        str++;
    }

    printf("%d",iCount);
}
int main()
{
    char arr[20];

    printf("Enter the string : ");
    scanf("%[^\n]",arr);

    CountSpace(arr);

    return 0;
}
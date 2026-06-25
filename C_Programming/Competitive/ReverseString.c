/*
Write a program which accept string from user and 
reverse that string in place
*/

#include<stdio.h>

void StrRevX(char *str)
{
    char *start = NULL;
    char *end = NULL;
    char temp = '\0';
    start = str;

    while(*str != 0)
    {
        str++;
    } 
    str--;
    end = str;

    while(start < end)
    {
        temp = *start;
        *start = *end;
        *end = temp;

        start++;
        end--;
    }
}
int main()
{
    char arr[20];

    printf("Enter the string : ");
    scanf("%[^'\n']s",arr);

    StrRevX(arr);
    printf("Modified String is %s",arr);

    return 0;
}
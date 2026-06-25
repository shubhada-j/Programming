/*
Write a program which accept string from user and copy the contents of that string into another string.
*/
#include<stdio.h>

void StrCpy(char *src, char *dest)
{
    while(*src != '\0')
    {
        *dest = *src;
        src++;
        dest++;
    }
    *dest = '\0';
}

int main()
{
    char arr[30];
    char brr[30];
    
    printf("Enter the String : ");
    scanf("%[^'\n]s",arr);

    StrCpy(arr,brr);

    printf("String is : %s",brr);

    return 0;
}
/*
Write a program which 2 strings from user and 
concat second string after first string
*/

#include<stdio.h>

void StrCatX(char *src, char *dest)
{
    while(*dest != '\0')
    {
        dest++;
    }
    while(*src != '\0')
    {
        *dest = *src;
        dest++;
        src++;
    }
    *dest ='\0';
}

int main()
{
    char arr[50];
    char brr[50];

    printf("Enter the String : ");
    scanf("%[^'\n]s",arr);

    getchar();

    printf("Enter the String : ");
    scanf(" %[^'\n]s",brr);

    StrCatX(brr,arr);
    
    printf("String is : %s",arr);

    return 0;
}
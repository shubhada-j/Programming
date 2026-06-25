/*
Write a program which accept string from user and 
copy samll characters of that string into another string
*/

#include<stdio.h>

void StrCpyCap(char *src,char *dest)
{
    while(*src != '\0')
    {
        if((*src >= 'a') && (*src <= 'z'))
        {
            *dest = *src;
            *dest++;
        }
        *src++;
    }
    *dest = '\0';
}

int main()
{
    char arr[30];
    char brr[30];

    printf("Enter the String : ");
    scanf("%[^'\n]s",arr);

    StrCpyCap(arr,brr);

    printf("String is : %s",brr);

    return 0;
}
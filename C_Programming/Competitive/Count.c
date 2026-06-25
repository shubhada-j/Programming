/*
Write a program which accept string from user and 
copy the contents of that string into another string 
and print the characters till the index user wants.
*/

#include<stdio.h>

void StrNCpyX(char *src, char*dest, int iCnt)
{

    while((*src != '\0') && (iCnt != 0))
    {
        *dest = *src;
        *src++;
        *dest++;
        iCnt--;

    }
    *dest = '\0';
}

int main()
{
    char arr[30];
    char brr[30];
    int iValue = 0;
    
    printf("Enter the String : ");
    scanf("%[^'\n]s",arr);

    printf("Enter no. of characters to copy : ");
    scanf("%d",&iValue);

    StrNCpyX(arr,brr,iValue);

    printf("String is : %s",brr);

    return 0;
}
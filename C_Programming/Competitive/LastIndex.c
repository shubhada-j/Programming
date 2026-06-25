/*
Write a program which accept string from user and accept one character 
Return index of last occurrence of that character
*/

#include<stdio.h>

int LastChar(char *str, char ch)
{
    int iCnt = 0;
    int iCount = -1;

    while(*str != 0)
    {
        if(*str == ch)
        {
            iCount = iCnt;
        }
        iCnt++;
        str++;
    } 
    return iCount;
}
int main()
{
    char arr[20];
    char cValue;
    int iRet = 0;

    printf("Enter the string : ");
    scanf("%[^'\n']s",arr);

    printf("Enter the character : ");
    scanf(" %c",&cValue);

    iRet = LastChar(arr,cValue);

    printf("Character location is %d",iRet);

    return 0;
}
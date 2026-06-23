//Write a program which accept string from user and check wjether it contains vowels in it or not

#include<stdio.h>
#define TRUE 1
#define FALSE 0
typedef int BOOL;

BOOL ChkVowel(char *str)
{
    while(*str != '\0')
    {
        if((*str == 'a') || (*str == 'e') || (*str == 'i') || (*str == 'o') ||(*str == 'u') ||
        (*str == 'A') || (*str == 'E') || (*str == 'I') || (*str == 'O') ||(*str == 'U'))
        {
            return TRUE;
        }
        str++;
    }
    return FALSE;
}

int main()
{
    char arr[20];
    BOOL bRet = FALSE;

    printf("Enter the String : ");
    scanf("%[^`\n`]s",arr);

    bRet = ChkVowel(arr);

    if(bRet == TRUE)
    {
        printf("Contains Vowels");
    }
    else
    {
        printf("There is no Vowels");
    }
    return 0;
}
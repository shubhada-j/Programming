/*
Accept the character from user an check wheather it is special symbol or not
(!,@,#,$,%,^,&,*)
*/

#include<stdio.h>
#define TRUE 1
#define FALSE 0
typedef int BOOL;

BOOL ChkSpcial(char ch)
{
    if(ch >= '!' && ch <= '*')
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}
int main()
{
    char cValue = '\0';
    BOOL bRet = FALSE;
    
    printf("Enter the character : \n");
    scanf("%c",&cValue);
    
    bRet = ChkSpcial(cValue);

    if(bRet == TRUE)
    {
        printf("It is special symbol");
    }
    else
    {
        printf("It is not special symbol");
    }

    return 0;
}
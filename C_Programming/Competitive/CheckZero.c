/*

Accept the number from user and check whether it contains 0 in it or not

Input  : 2395
Output : There is no Zero

Input  : 1018
Output : It contains Zero

Input  : 9000
Output : It contains Zero

Input  : 10687
Output : It contains Zero

*/

#include<stdio.h>

#define TRUE 1
#define FALSE 0

typedef int BOOL;

BOOL ChkZero(int iNo)
{
    int iDigit = 0;

    while(iNo)
    {
        iDigit = iNo % 10;

        if(iDigit == 0)
        {
            return TRUE;
        }
        else
        {
            return FALSE;
        }

        iNo = iNo / 10;

    }

}

int main()
{
    int iValue = 0;
    BOOL bRet = FALSE;

    printf("Enter number : ");
    scanf("%d",&iValue);

    bRet = ChkZero(iValue);

    if(bRet == TRUE)
    {
        printf("It contains Zero");
    }
    else
    {
        printf("There is no Zero");
    }

    return 0;
}

// Time Complexity : O(N)
// Where N >= 0
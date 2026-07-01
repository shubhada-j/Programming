//Write a program which accept one number, two positions from user and check whether bit at first or bit at second position is ON or OFF

#include <stdio.h>

typedef unsigned int UINT;
typedef int BOOL;

#define TRUE 1
#define FALSE 0

BOOL ChkBit(UINT iNo, UINT iPos1, UINT iPos2)
{
    UINT iMask1 = 0;
    UINT iMask2 = 0;
    UINT iMask = 0;
    UINT iResult = 0;

    if((iPos1 < 1 || iPos1 > 32) || (iPos2 < 1 || iPos2 > 32))
    {
        printf("Invalid Position\n");
        return FALSE;
    }

    iMask1 = 1 << (iPos1 - 1);
    iMask2 = 1 << (iPos2 - 1);

    iMask = iMask1 | iMask2;

    iResult = iNo & iMask;

    if(iResult != 0)
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
    UINT iValue = 0;
    UINT iPos1 = 0, iPos2 = 0;
    BOOL bRet = FALSE;

    printf("Enter number : ");
    scanf("%d", &iValue);

    printf("Enter first position : ");
    scanf("%d", &iPos1);

    printf("Enter second position : ");
    scanf("%d", &iPos2);

    bRet = ChkBit(iValue, iPos1, iPos2);

    if(bRet == TRUE)
    {
        printf("At least one of the bits is ON\n");
    }
    else
    {
        printf("Both bits are OFF\n");
    }

    return 0;
}
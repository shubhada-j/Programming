//Write a program which accept one number and position from user and toggle that bit.Return updated number

#include<stdio.h>

typedef unsigned int UINT;

UINT ToggleBit(UINT iNo, UINT iPos)
{
    UINT iMask = 0x1;
    UINT iResult = 0;

    iMask = iMask << (iPos -1);

    iResult = iMask ^ iNo;

    return iResult;
}

int main()
{
    UINT iValue = 0;
    UINT iLocation = 0;
    UINT iRet = 0;

    printf("Enter the number : ");
    scanf("%d",&iValue);

    printf("Enter the position : ");
    scanf("%d",&iLocation);

    iRet = ToggleBit(iValue, iLocation);

    printf("Updated number is : %d",iRet);
}
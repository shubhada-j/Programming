//Write a program which accept one number from user and toggle contents of first bit of last nibble of that number.Return updated number

#include<stdio.h>

typedef unsigned int UINT;

UINT ToggleBit(UINT iNo)
{
    UINT iMask = 0x8;
    UINT iResult = 0;

    iResult = iMask ^ iNo;

    return iResult;
}

int main()
{
    UINT iValue = 0;
    UINT iRet = 0;

    printf("Enter the number : ");
    scanf("%d",&iValue);

    iRet = ToggleBit(iValue);
    printf("Updated number is : %d",iRet);
}
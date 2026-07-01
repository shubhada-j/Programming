//Write a program which accept one number and range of position from user. Toggle all bits from that range.

#include<stdio.h>

typedef unsigned int UINT;

UINT ToggleBitRange(UINT iNo, UINT iStart, UINT iEnd)
{
    UINT iMask = 0;
    UINT iResult = 0;
    UINT iCnt = 0;

    for(iCnt = iStart; iCnt <=iEnd; iCnt++)
    {
        iMask = iMask | (1 << (iCnt -1));
    }

    iResult = iMask ^ iNo;

    return iResult;
}

int main()
{
    UINT iValue = 0;
    UINT iRStart = 0;
    UINT iREnd = 0;
    UINT iRet = 0;

    printf("Enter the number : ");
    scanf("%d",&iValue);

    printf("Enter the starting of range : ");
    scanf("%d",&iRStart);

    printf("Enter the ending of range : ");
    scanf("%d",&iREnd);

    iRet = ToggleBitRange(iValue, iRStart, iREnd);

    printf("Updated number is : %d",iRet);
}
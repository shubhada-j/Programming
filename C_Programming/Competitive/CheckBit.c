//Write a program which accept one number and position from user and check whether bit at that position is ON or OFF. If bit is ON return TRUE otherwise FALSE.

#include<stdio.h>

typedef unsigned int UINT;
typedef int BOOL;

#define TRUE 1
#define FALSE 0

BOOL ChkBit(UINT iNo,UINT iPos)
{
    UINT iMask = 0x1;
    UINT iResult = 0;       

    if(iPos < 1 || iPos > 32)
    {
        printf("Invalid Bit Position\n");
        return iNo;
    }

    iMask = iMask <<(iPos - 1);

    iResult = iNo & iMask;

    if(iResult == iMask)
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
    BOOL BRet = 0;
    UINT iLocation = 0x1;

    printf("Enter Number : \n");
    scanf("%d",&iValue);

    printf("Enter the position : \n");
    scanf("%d",&iLocation);

    BRet = ChkBit(iValue,iLocation);
    
    if(BRet == TRUE)
    {
        printf("Bit is ON\n");
    }
    else
    {
        printf("Bit is OFF\n");
    }
    
    return 0;
}




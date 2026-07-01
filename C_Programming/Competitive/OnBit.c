//Write a program which accept one number and position from user and ON that bit. Return modified number

#include<stdio.h>
typedef unsigned int UINT;

UINT ONBit(UINT iNo,UINT iPos)
{
    UINT iMask = 0x1;
    UINT iResult = 0;       

    if(iPos < 1 || iPos > 32)
    {
        printf("Invalid Bit Position\n");
        return iNo;
    }

    iMask = iMask <<(iPos - 1);

    iResult = iNo | iMask;

    return iResult;

}
int main()
{
    UINT iValue = 0;
    UINT iRet = 0;
    UINT iLocation = 0x1;

    printf("Enter Number : \n");
    scanf("%d",&iValue);

    printf("Enter the position : \n");
    scanf("%d",&iLocation);

    iRet = ONBit(iValue,iLocation);

    printf("Updated number is : %d",iRet);
    
    return 0;
}




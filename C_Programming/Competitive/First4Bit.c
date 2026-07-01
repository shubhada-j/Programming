//Write a program which accept one number from user and ON its first 4 bits. Return modified number

#include<stdio.h>
typedef unsigned int UINT;

UINT ONBit(UINT iNo)
{
    UINT iMask = 0xF;
    UINT iResult = 0;       

    iResult = iNo | iMask;

    return iResult;

}
int main()
{
    UINT iValue = 0;
    UINT iRet = 0;

    printf("Enter Number : \n");
    scanf("%d",&iValue);

    iRet = ONBit(iValue);

    printf("Updated number is : %d",iRet);
    
    return 0;
}




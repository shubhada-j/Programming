//Write a program which accept one number from user and OFF 7th and 10th bit of that number if it is on. Return modified number

#include<stdio.h>
typedef unsigned int UINT;

UINT OFFBit(UINT iNo)
{
    UINT iMask = 0xFFFFFDBF;
    UINT iResult = 0;       

    iResult = iNo & iMask;

    return iResult;

}
int main()
{
    UINT iValue = 0;
    UINT iRet = 0;

    printf("Enter Number : \n");
    scanf("%d",&iValue);

    iRet = OFFBit(iValue);

    printf("Updated number is : %d",iRet);
    
    return 0;
}




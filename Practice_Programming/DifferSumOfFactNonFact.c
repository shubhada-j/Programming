/*

Accept number from user and return difference between summation of all its factors and non factors

Input  : 12
Output : -22    (28-50)

Input  : 10
Output : -19    (18-37)

*/

#include<stdio.h>

int FactDiff(int iNo)
{
    int iCnt = 0;
    int iNonFactSum = 0;
    int iFactSum = 0;
    int iDiff = 0;


    for(iCnt = 1; iCnt<=iNo; iCnt++)
    {
        if(iNo % iCnt != 0)
        {
            iNonFactSum = iNonFactSum + iCnt;
        }
        else if(iNo % iCnt == 0)
        {
            iFactSum = iFactSum + iCnt;
        }
    }
    
    iDiff = iFactSum - iNonFactSum;
    return iDiff;
}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter number : ");
    scanf("%d",&iValue);

    iRet = FactDiff(iValue);

    printf("%d",iRet);

    return 0;
}
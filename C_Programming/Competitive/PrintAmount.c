/*

Accept amount in US dollar and return its corresponding value in Indian Currency.
Consider 1$ as 70 rupees.

Input  : 10
Output : 700

Input  : 3
Output : 210

Input  : 1200
Output : 84000

*/

#include<stdio.h>

int DollarToINR(int iNo)
{
    int iCnt = 0;
    int iAmt = 0;

    for(iCnt = iNo; iCnt<=iNo; iCnt++)
    {
        iAmt = iCnt * 70;
    }

    return iAmt;
}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter number of USD : ");
    scanf("%d",&iValue);

    iRet = DollarToINR(iValue);

    printf("Value in INR is %d",iRet);

    return 0;
}
// Time Complexity : O(N)
// Where N >= 0
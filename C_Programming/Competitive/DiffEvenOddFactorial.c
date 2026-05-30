/*
Accept the number from user and returns the difference between even factorial and odd factorial of given number

Input  : 5
Output : -7      (8 - 15)

Input  : -5
Output : -7      (8 - 15)

Input  : 10
Output : 2895    (3840 - 945)

*/

#include<stdio.h>

int FactorialDiff(int iNo)
{
    int iCnt = 1;
    int iDiff = 0;
    int iEvenFact = 1;
    int iOddFact = 1;

    if(iNo < 0)
    {
        iNo = -iNo;
    }

    for(iCnt = 1; iCnt <= iNo; iCnt++)
    {
        if(iCnt % 2 == 0)
        {
            iEvenFact = iEvenFact * iCnt;
        }
        
        else if(iCnt % 2 != 0)
        {
            iOddFact = iOddFact * iCnt;
        }

        iDiff = iEvenFact - iOddFact;
    }

    return iDiff;
}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter number : ");
    scanf("%d",&iValue);

    iRet = FactorialDiff(iValue);

    printf("Factorial difference is %d",iRet);

    return 0;
}

// Time Complexity : O(N)
// Where N >= 0
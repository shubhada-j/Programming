/*

Accept area in square feet and convert it into square meter.
(1 Square feet = 0.0929 Square meter)

Input  : 5
Output : 0.464515

Input  : 7
Output : 0.650321

*/

#include<stdio.h>

double SquareMeter(int iNo)
{
    double dArea = 0.00;

    dArea = 0.0929 * iNo;

    return dArea;
}
int main()
{
    int iValue = 0;
    double dRet = 0.0;

    printf("Enter area in square feet : ");
    scanf("%d",&iValue);

    dRet = SquareMeter(iValue);

    printf("%d square feet is equal to %lf square meter",iValue,dRet);

    return 0;
}

// Time Complexity : O(1)

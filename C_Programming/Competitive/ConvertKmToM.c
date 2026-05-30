/* 
Accept the distance in kilometer and convert it into meter
(1 Kilometer = 1000 Meter)

Input  : 5
Output : 5000

Input  : 12
Output : 12000

*/

#include<stdio.h>

int KMtoMeter(int iNo)
{
    int iDistance = 0;

    iDistance = iNo * 1000;

    return iDistance;
}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter Distance : ");
    scanf("%d",&iValue);

    iRet = KMtoMeter(iValue);

    printf("%d Kilometer is equal to %d Meter",iValue,iRet);
}

// Time Complexity : O(1)

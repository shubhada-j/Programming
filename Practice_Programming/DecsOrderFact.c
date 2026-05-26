/*
Accept the number from user and dispaly its factor in decresing order

Input  : 12
Output : 6 4 3 2 1

Input  : 13
Output : 1

Input  : 10
Output : 5 2 1

*/

#include<stdio.h>

void FactRev(int iNo)
{
    int iCnt = 0;

    for(iCnt = iNo/2; iCnt<=iNo; iCnt--)
    {
        if(iNo % iCnt == 0)
        {
            printf("%d\t",iCnt);
        }
    }
}

int main()
{
    int iValue = 0;

    printf("Enter number : ");
    scanf("%d",&iValue);

    FactRev(iValue);

    return 0;
}
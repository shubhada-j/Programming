// Write a program which accept two numbers from user and display position of common ON bits from that two number 

#include<stdio.h>
typedef unsigned int UINT;

void CommonBits(UINT iNo1, UINT iNo2)
{
    UINT iResult = 0;
    UINT iPos = 1;

    iResult = iNo1 & iNo2;

    while(iResult != 0)
    {
        if((iResult & 1) == 1)
        {
            printf("%d\t",iPos);
        }

        iPos++;
        iResult = iResult >> 1;
    }
    printf("\n");

}

int main()
{
    UINT iValue1 = 0;
    UINT iValue2 = 0;

    printf("Enter the first number : ");
    scanf("%d",&iValue1);

    printf("Enter the second number : ");
    scanf("%d",&iValue2);

    CommonBits(iValue1,iValue2);

    return 0;
}
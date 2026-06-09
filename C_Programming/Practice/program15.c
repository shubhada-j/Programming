#include<stdio.h>
#include<stdbool.h>

bool CheckEvenOdd(int iNo)
{
    int iRemainder = 0;

    iRemainder = iNo % 2;

    if(iRemainder == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    int iValue = 0;
    bool bRet = false;         //false internally treated as 0 so here we write default value of bool is false

    printf("Enter number to check whether it is Even or Odd : ");
    scanf("%d",&iValue);

    bRet = CheckEvenOdd(iValue);
    
    if(bRet == true)
    {
        printf("%d is even\n",iValue);
    }
    else
    {
        printf("%d is odd\n",iValue);
    }

    return 0;
}
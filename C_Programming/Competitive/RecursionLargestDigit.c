//Write a recursive program which accept the number from user and return the largest digit
// Input  : 87983
// Output : 9

#include<stdio.h>

int Max(int iNo)
{
    static int iDigit = 0;
    static int iMax = 0;

    if(iNo != 0)
    {
        iDigit = iNo % 10;
        
        if(iDigit > iMax)
        {
            iMax = iDigit;
        }

        iNo = iNo / 10;

        Max(iNo);
    }

    return iMax;
}
int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter the Value : ");
    scanf("%d",&iValue);

    iRet = Max(iValue);
    printf("Largest Digit is : %d",iRet);

    return 0;
}
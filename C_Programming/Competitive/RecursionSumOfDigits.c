//Write a recursive program which accept the number from user and return the summation of digits
// Input  : 879
// Output : 24

#include<stdio.h>

int Sum(int iNo)
{
    static int iDigit = 0;
    static int iSum = 0;


    if(iNo != 0)
    {
        iDigit = iNo % 10;
        iSum = iSum + iDigit;
        iNo = iNo / 10;

        Sum(iNo);
    }

    return iSum;
}
int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter the Value : ");
    scanf("%d",&iValue);

    iRet = Sum(iValue);
    printf("Sum of Digits : %d",iRet);

    return 0;
}
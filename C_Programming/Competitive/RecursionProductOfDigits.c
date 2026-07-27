//Write a recursive program which accept the number from user and return the product of digits
// Input  : 523
// Output : 30

#include<stdio.h>

int Mult(int iNo)
{
    static int iDigit = 0;
    static int iMult = 1;


    if(iNo != 0)
    {
        iDigit = iNo % 10;
        iMult = iMult * iDigit;
        iNo = iNo / 10;

        Mult(iNo);
    }

    return iMult;
}
int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter the Value : ");
    scanf("%d",&iValue);

    iRet = Mult(iValue);
    printf("Product of Digits : %d",iRet);

    return 0;
}
//Write a recursive program which accept the number from user and return the reverse number
// Input  : 523
// Output : 325

#include<stdio.h>

int Reverse(int iNo)
{
    static int iDigit = 0;
    static int iNum = 0;

    if(iNo != 0)
    {
        iDigit = iNo % 10;
        iNum = (iNum * 10) + iDigit;
        iNo = iNo / 10;

        Reverse(iNo);
    }

    return iNum;
}
int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter the Value : ");
    scanf("%d",&iValue);

    iRet = Reverse(iValue);
    printf("Reverse number is : %d",iRet);

    return 0;
}
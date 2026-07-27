//Write a recursive program which accept the number from user and returns its factorial
// Input  : 5
// Output : 120

#include<stdio.h>

int Fact(int iNo)
{
    static int i = 1;
    static int iFact = 1;

    if(i <= iNo)
    {
        iFact = iFact * i;
        i++;

        Fact(iNo);
    }

    return iFact;
}
int main()
{
    int iValue = 0;
    int iRet = 0;
    
    printf("Enter the Number : ");
    scanf("%d",&iValue);

    iRet = Fact(iValue);
    printf("Factprial is : %d",iRet);

    return 0;
}
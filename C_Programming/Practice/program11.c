/*
Algorithm:

    START
        Accept the number as No
        If No is completely divisible by 2
            then print Even
        otherwise
            pint odd
    STOP

    START
        Accept the number as No
        Divide No by 2
        If remainder is 0
            then print as Even
        otherwise
            print as odd  
    STOP
*/

#include<stdio.h>

int main()
{
    int iValue = 0;
    int iRemainder = 0;

    printf("Enter number : \n");
    scanf("%d",&iValue);

    iRemainder = iValue % 2;

    if(iRemainder == 0)
    {
        printf("Number is Even\n");
    }
    else
    {
        printf("Number is odd\n");
    }

    return 0;
}
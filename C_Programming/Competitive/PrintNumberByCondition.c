/*
Accept number from user and if number is less than 50 then print small, if it is greater than 50 and less than 100 then print medium, if it is greater than 100 then print large

Input  : 75
Output : Medium

*/

#include<stdio.h>

void Number(int iNo)
{
    if(iNo<50)
    {
        printf("small\n");
    }
    else if ((50<iNo) && (iNo<100))
    {
        printf("medium\n");
    }
    else
    {
        printf("large");
    }
    
}

int main()
{
    int iValue = 0;

    printf("Enter Number : ");
    scanf("%d",&iValue);

    Number(iValue);

    return 0;
}

// Time Complexity : O(1)

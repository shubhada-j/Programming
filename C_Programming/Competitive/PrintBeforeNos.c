/*
Accept the number from user and print the numbers till that number 

Input  : 8
Output : 1 2 3 4 5 6 7 8 

*/

#include<stdio.h>

void Display(int iNo)
{
    int iCnt = 0;

    for(iCnt = 1; iCnt <=iNo; iCnt++)
    {
        printf("%d\t",iCnt);
    }
}

int main()
{
    int iValue = 0;

    printf("Enter number : ");
    scanf("%d",&iValue);

    Display(iValue);

    return 0;
}

// Time Complexity : O(N)
// Where N >= 0
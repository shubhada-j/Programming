/*
Accept the number from user and print first 5 multiples of N

Input  : 4
Output : 4 8 12 16 20 

*/

#include<stdio.h>

void MultipleDisplay(int iNo)
{
    int iCnt = 0;
    int iMult = 0;
    
    for(iCnt = 1; iCnt<=5; iCnt++)
    {
       iMult = iNo*iCnt;
       printf("%d\t",iMult);
    
    }
}
int main()
{
    int iValue = 0;
    
    printf("Enter number : ");
    scanf("%d",&iValue);
    
    MultipleDisplay(iValue);
    
    return 0;
}

// Time Complexity : O(N)
// Where N >= 0
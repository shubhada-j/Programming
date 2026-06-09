//////////////////////////////////////////////////////////////////////
//
// Include required header files
//
/////////////////////////////////////////////////////////////////////

#include<stdio.h>
#include<stdbool.h>

/////////////////////////////////////////////////////////////////////
// 
// Function name :  CheckEvenOdd
// Input :          int
// Output :         int,String 
// Description :    Checking the number is even or odd
// Date :           10/05/2026
// Author :         Shubhada Balasaheb Jadhav
//
/////////////////////////////////////////////////////////////////////

bool CheckEvenOdd(int iNo)
{
    if((iNo % 2) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

/////////////////////////////////////////////////////////////////////
//
//  Application to cjeck number is even or odd
//
/////////////////////////////////////////////////////////////////////

int main()
{
    int iValue = 0;
    bool bRet = false;  

    printf("Enter number to check whether it is Even or Odd : ");
    scanf("%d",&iValue);

    bRet = CheckEvenOdd(iValue);
    
    if(bRet)
    {
        printf("%d is even\n",iValue);
    }
    else
    {
        printf("%d is odd\n",iValue);
    }

    return 0;
}

/////////////////////////////////////////////////////////////////////
//
// Input :    10
// Output :   10 is even
//
/////////////////////////////////////////////////////////////////////

//logical && logical || truthtable 
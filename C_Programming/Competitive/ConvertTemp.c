/*
Accept temprature in Fahrenheit and convert it into celsius.
(1 celsius = (Fahrenheit - 32) * (5/9))

Input  : 10
Output : -12.2222 (!0-32) * (5/9)

Input  : 34
Output : 1.11111 (34-32) * (5/9)

*/

#include<stdio.h>

double FhtoCs (float fTemp)
{
    double dTemp = 0.0;

    dTemp = ((fTemp - 32.0) * (5.0/9.0));

    return dTemp;

}

int main()
{
    float fValue = 0.0;
    double dRet = 0.0;

    printf("Enter temprature in Fahrenheit : ");
    scanf("%f",&fValue);

    dRet = FhtoCs(fValue);

    printf("%f Fahrenheit is equal to %lf Celsius",fValue,dRet);

    return 0;
}

// Time Complexity : O(1)
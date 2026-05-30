/*
Accept the radius of circle from user and calculate its area
Consider value of PI as 3.14 (Area = PI * Radius * Radius)

Input  : 5.3
Output : 88.2026

Input  : 10.4
Output : 339.6224

*/

#include<stdio.h>

double CircleArea(float fRadius)
{
    float PI = 3.14f;
    double dArea = 0;

    dArea = (PI * fRadius * fRadius);

    return dArea;
}

int main()
{
    float fValue = 0.0f;
    double dRet = 0.0;

    printf("Enter radius : ");
    scanf("%f",&fValue);

    dRet = CircleArea(fValue);

    printf("Area of Circle is : %lf",dRet);

    return 0;
}

// Time Complexity : O(1)

/*
    Algorithm

    START
        Accept first number as No1
        Accept second number as No2
        Perform Addition of No1 and No2
        Display the Result
    STOP
*/

#include<stdio.h>

int main()
{                           
    /*changing the datatype int -> float 
    because in int point valus cannot accepeted*/
    float i,j,k;

    printf("Enter first number : \n");
    scanf("%f",&i);

    printf("Enter second number : \n");
    scanf("%f",&j);

    k = i + j;
    
    printf("Addition is : %f\n",k);

    return 0;
}
/*
Write a program which accept string from user and return difference between 
frequency of small characters and frequency of capital characters.
*/

#include<stdio.h>

int Difference(char *str)
{
    int iSmallCount = 0;   
    int iCapitalCount = 0; 

    while(*str != '\0')
    {
        if(*str >= 'A' && *str <= 'Z')
        {
            iCapitalCount++;
        }
        else if((*str >= 'a') && (*str <= 'z'))
        {
            iSmallCount++;
        }
        str++;
    }

    return(iSmallCount - iCapitalCount);
}

int main()
{
    char arr[20];
    int iRet = 0;

    printf("Enter the String : ");
    scanf("%[^`\n`]s",arr);

    iRet = Difference(arr);

    printf("Difference is : %d",iRet);

    return 0;
}
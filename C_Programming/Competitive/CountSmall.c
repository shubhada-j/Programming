//Write a program which accepts string from user and count number of small characters.

#include<stdio.h>
int CountCapital(char *str)
{
    int iCount = 0;
    int iCnt = 0;

    while(*str != 0)
    {
        if(*str >= 'a' && *str <= 'z')
        {
            iCount++;
        }
        str++;
    }
    return iCount;
}

int main()
{
    char arr[50];
    int iRet = 0;

    printf("Enter the character : \n");
    scanf("%[^`\n`]s",arr);

    iRet = CountCapital(arr);
    printf("The frequency is : %d",iRet);

    return 0;
}
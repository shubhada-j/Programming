//Write a recursive program which accept the string from user and count the no. of characters
// Input  : Hello
// Output : 5

#include<stdio.h>

int Strlen(char *str)
{
    static int iCount = 0;

    if(*str != '\0')
    {   
        iCount++;
        str++;  

        Strlen(str);
    }

   return iCount;
}
int main()
{
    int iRet = 0;
    char Arr[20];
    
    printf("Enter the String : ");
    scanf("%s",Arr);

    iRet = Strlen(Arr);
    printf("No of Characters : %d",iRet);

    return 0;
}
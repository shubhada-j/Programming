//Write a recursive program which accept the string from user and count the small characters
// Input  : HElloWOrlD
// Output : 5

#include<stdio.h>

int Strlen(char *str)
{
    static int iCount = 0;

    if(*str != '\0')
    {   
        if(*str >= 'a' && *str <= 'z')
        {
            iCount++;
        }

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
    scanf("%[^\n]",Arr);

    iRet = Strlen(Arr);
    printf("No of small charcters are : %d",iRet);

    return 0;
}
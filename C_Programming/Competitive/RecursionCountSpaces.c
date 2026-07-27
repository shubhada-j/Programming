//Write a recursive program which accept the string from user and count the white spaces
// Input  : HE llp WOr ID
// Output : 3

#include<stdio.h>

int Strlen(char *str)
{
    static int iCount = 0;

    if(*str != '\0')
    {   
        if(*str == ' ')
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
    printf("No of White Spaces are : %d",iRet);

    return 0;
}
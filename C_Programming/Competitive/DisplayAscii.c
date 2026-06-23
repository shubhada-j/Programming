/*
Accept character from user If character is small display its corressponding capital character 
and if it small then display its corresponding capital In other cases display as it is 
*/

#include<stdio.h>
void Display(char ch)
{
    if( ch >= 97 && ch <= 122)
    {
        ch = ch - 32;
        printf("Character is : %c",ch);
    }
    else
    {
        printf("Chracter is : %c",ch);
    }
}
int main()
{
    char cValue = '\0';

    printf("Enter the character : \n");
    scanf("%c",&cValue);

    Display(cValue);

    return 0;
}

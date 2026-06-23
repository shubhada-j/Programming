/*
Accept character from user. If it is capital then display all the characters from the input characters till Z.
If the input character is small then print the all characters in reverse order till a In other cases return directly.
*/

#include<stdio.h>

void Display(char ch)
{

    if(ch >= 'A' && ch <= 'Z')
    {
        while (ch <=90)
        {
            printf("%c",ch);
            ch++;
        }
    }
    else if(ch >= 'a' && ch <= 'z')
    {
        while (ch <=122 && ch>= 97)
        {
            printf("%c",ch);
            ch--;
        } 
    }
}

int main()
{
    char cValue = '\0';

    printf("Enter the characters : \n");
    scanf("%c",&cValue);
    
    Display(cValue);
    
    return 0;
}
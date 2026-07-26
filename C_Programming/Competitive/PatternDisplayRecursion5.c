//Write a recursive program which display below pattern
// Output :  a b c d e f

#include<stdio.h>

void Display()
{
    static int i = 0;
    static char  letter = 'a';


    if(i < 6)
    {
        printf("%c\t",letter);
        i++;
        letter++;

        Display();
    }
}
int main()
{
    
    Display();

    return 0;
}
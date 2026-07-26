//Write a recursive program which display below pattern
// Output : A   B   C   D   E   F

#include<stdio.h>

void Display()
{
    static int i = 0;
    static char  letter = 'A';


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
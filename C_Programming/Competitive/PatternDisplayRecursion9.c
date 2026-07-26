//Write a recursive program which display below pattern
// Output : A   B   C   D   E   F

#include<stdio.h>

void Display(int iNo)
{
    static int i = 0;
    static char  letter = 'A';

    if(i < iNo)
    {
        printf("%c\t",letter);
        i++;
        letter++;

        Display(iNo);
    }
}
int main()
{
    int iValue = 0;

    printf("Enter the size : ");
    scanf("%d",&iValue);
    
    Display(iValue);

    return 0;
}
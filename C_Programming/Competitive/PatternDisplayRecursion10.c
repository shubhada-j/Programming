//Write a recursive program which display below pattern
// Output : a b c d e f

#include<stdio.h>

void Display(int iNo)
{
    static int i = 0;
    static char  letter = 'a';

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
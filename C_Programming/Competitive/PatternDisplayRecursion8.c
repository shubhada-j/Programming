//Write a recursive program which display below pattern
// Output : 5   4   3   2   1

#include<stdio.h>

void Display(int iNo)
{
    static int i = 1;
   
    if(i <= iNo)
    {
        printf("%d\t",iNo);
        iNo--;

        Display(iNo);
    }
}
int main()
{
    int iValue = 0;

    printf("Enter the number : \n");
    scanf("%d",&iValue);

    Display(iValue);

    return 0;
}
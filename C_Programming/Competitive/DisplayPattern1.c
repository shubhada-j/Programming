//Input  : 5
//Output : A B C D E

#include<stdio.h>
void Pattern(int iNo)
{
    int iCnt = 0;
    char Ch = '\0';

    for(iCnt = 1, Ch = 'A'; iCnt <= iNo; iCnt++,Ch++)
    {
        printf("%c\t",Ch);
    }
}

int main()
{
    int iValue = 0;
    printf("Enter number of elements : ");
    scanf("%d",&iValue);

    Pattern(iValue);

    return 0;
}
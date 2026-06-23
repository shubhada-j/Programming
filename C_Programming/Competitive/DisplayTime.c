/*Accept division of student from user and depends on the division display exam timing.
There are 4 divisions in school as A,B,C,D. 
Exam of division A at 7 AM, B at 8.30 AM, C at 9.20AM and D at 10.30AM.
(Application should be case insensitive) 
*/

#include<stdio.h>
void Division(char Ch)
{
    if(Ch == 'A' || Ch == 'a') 
    {
        printf("Exam Time is : 7 AM");
    }
    else if(Ch == 'B' || Ch == 'b') 
    {
        printf("Exam Time is : 8.30 AM");
    }
    else if(Ch == 'C' || Ch == 'c') 
    {
        printf("Exam Time is : 9.20 AM");
    }
    else if(Ch == 'D' || Ch == 'd') 
    {
        printf("Exam Time is : 10.30 AM");
    }
    else
    {
        printf("Incorrect Input");
    }

}
int main()
{
    char cDiv = '\0';

    printf("Enter Your Divsion : ");
    scanf("%c",&cDiv);

    Division(cDiv);

    return 0;
}
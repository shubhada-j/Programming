/*

Accept N numbers from user and return difference between summation of even elements and summation of odd elements.

Input  : N        : 6
         Elememts : 85 66 3 80 93 88
         
Output : 53         (234 - 181)

*/

#include<stdio.h>
#include<stdlib.h>

int Difference(int Arr[], int iLength)
{
    int iCnt = 0;
    int iDiffer = 0;
    int iEvenSum = 0;
    int iOddSum = 0;

    for(iCnt = 0; iCnt < iLength; iCnt++)
    {
        if(Arr[iCnt] % 2 == 0)
        {
            iEvenSum = iEvenSum + Arr[iCnt];
        }
        else
        {
            iOddSum = iOddSum + Arr[iCnt];
        }
    }

    iDiffer = iEvenSum - iOddSum;
    return iDiffer;
}

int main()
{
    int iSize = 0;
    int iRet = 0;
    int iCnt = 0;

    int *p = NULL;

    //Accept the number of elements from user
    printf("Enter number of elements : ");
    scanf("%d",&iSize);

    //Allocate the memory 
    p = (int *)malloc(iSize * sizeof(int));

    if(p == NULL)
    {
        printf("Unable to allocate memoery");
        return -1;
    }

    //Accept the elements from user
    printf("Enter %d elements : \n",iSize);

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        printf("Enter element %d :  ",iCnt+1);
        scanf("%d",&p[iCnt]);
    }

    //Use the memory
    iRet = Difference(p,iSize);
    printf("Result is : %d",iRet);

    //Deallocate the memory
    free(p);

    return 0;
}
#include<stdio.h>
#include<stdlib.h>

int SecondLargest(int Arr[],int iSize)
{
    int i = 0;

    int Largest = Arr[0];   
    int Second = 0;

    for(i = 0; i < iSize; i++)
    {
        if(Arr[i] > Largest)
        {
            Second = Largest;   
            Largest = Arr[i];   
        }   
        else if(Arr[i] < Largest && Arr[i] > Second)
        {
            Second = Arr[i];
        }
    }

    return Second;
}

int main()
{
    int Arr[] = {10,30,40,15,5,20,45};

    int iSize = sizeof(Arr)/sizeof(Arr[0]);

    int iRet = SecondLargest(Arr,iSize);

    printf("%d",iRet);

    return 0;
}
    
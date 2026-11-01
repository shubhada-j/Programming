#include<stdio.h>

void MoveZeroToEnd(int Brr[], int Size)
{
    int i = 0;
    int j = Size-1;

    for(i = Size-1; i >= 0; i--)
    {
        if(Brr[i] != 0)
        {
            Brr[j] = Brr[i];
            j--;
        }
    }

    for(i = j; i >= 0; i--)
    {
        Brr[i] = 0;
    }

    for(i = 0; i < Size; i++)
    {
        printf("%d",Brr[i]);
    }

}

int main()
{
    int Arr[] = {1,4,0,5,0,0,3,2};

    int iSize = sizeof(Arr)/sizeof(Arr[0]);

    MoveZeroToEnd(Arr,iSize);

    return 0;

}
#include <stdio.h>

void MoveZeros(int Arr[], int iSize)
{
    int j = 0;

    // Move all non-zero elements to the beginning
    for(int i = 0; i < iSize; i++)
    {
        if(Arr[i] != 0)
        {
            Arr[j] = Arr[i];
            j++;
        }

    }

    // Fill remaining positions with zero
    for(int i = j; i < iSize; i++)
    {
        Arr[i] = 0;
    }

    // Display the final array
    for(int i = 0; i < iSize; i++)
    {
        printf("%d ", Arr[i]);
    }
}

int main()
{
    int Arr[] = {0, 1, 0, 3, 12, 0, 5};

    int iSize = sizeof(Arr) / sizeof(Arr[0]);

    MoveZeros(Arr, iSize);

    return 0;
}

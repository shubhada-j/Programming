//Write generic program to accept N values and reverse the contents

#include<iostream>
using namespace std;

template<class T>
void Reverse(T *arr, int iSize)
{
    int i = 0;

    for(i = iSize - 1; i >= 0; i--)
    {
        cout<<arr[i]<<"\t";
    }
    cout<<"\n";
}

int main()
{
    int i = 0;

    int arr[] = {10,20,30,10,30,40,10,40,10};

    for(i = 0; i < 9; i++)
    {
        cout<<arr[i]<<"\t";
    }
    cout<<"\n";

    Reverse(arr,9);
}
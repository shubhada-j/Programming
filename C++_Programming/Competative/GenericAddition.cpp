//Write a generic program to accept N values from user and return addition of that values

#include<iostream>
using namespace std;

template <class T>
T AddN(T*arr,int iSize)
{
    T sum;
    sum = 0;
    int i = 0;

    //Filter
    for(i = 0; i<iSize; i++)
    {
        sum = sum + arr[i];
    }

    return sum;
}

int main()
{
    int arr[] = {10,20,30,40,50};

    float brr[] = {10.0,3.7,9.8,8.7};

    int iSum = AddN(arr,5);
    cout<<iSum<<endl;

    float fSum = AddN(brr,4);
    cout<<fSum<<endl;

    return 0;
}
// Write a program to accept N values from user and return smallest values

#include<iostream>
using namespace std;

template<class T>
T Min(T *arr, int iSize)
{
    int i = 0;
    T ans = arr[0];

    for(i = 0; i < iSize; i++)
    {
        if(arr[i] < ans)
        {
            ans = arr[i];
        }
    }

    return ans;

}

int main()
{
    int arr[] = {10,20,30,40,50};

    float brr[] = {10.0,3.7,9.8,8.7};

    int iRet = Min(arr,5);
    cout<<iRet<<endl;

    float fRet = Min(brr,4);
    cout<<fRet<<endl;

    return 0;

}
//Write generic program to accept N values and search last occurrence of any specific value

#include<iostream>
using namespace std;

template<class T>
int SearchLast(T *arr, int iSize, T iNo)
{
    int i = 0;
    int index = -1;

    for(i = 0; i < iSize; i++)
    {
        if(arr[i] == iNo)
        {
            index = i;
        }
    }

    return index;
}

int main()
{
    int arr[] = {10,20,30,10,30,40,10,40,10};
    int iRet = SearchLast(arr,9,1);
    cout<<iRet<<"\n";
    return 0;
}
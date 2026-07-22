//Write generic program to find largest number from three numbers

#include<iostream>
using namespace std;

template<class T>
T Max(T no1, T no2, T no3)
{
    if((no1 > no2) && (no1 > no3))
    {
        return no1;
    }
    else if((no2 > no1) && (no2 > no3))
    {
        return no2;
    }
    else
    {
        return no3;
    }
}

int main()
{
    cout<<Max(20,15,30)<<endl;
    cout<<Max(10.4,10.3,10.2)<<endl;

    return 0;
}
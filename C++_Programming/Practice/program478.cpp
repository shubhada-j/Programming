//ternary oprator

#include<iostream>
using namespace std;

template<class T>
T Maximum(T No1, T No2)
{
    T Ans;

    if(No1 > No2)
    {
        Ans = No1;
    }
    else
    {
        Ans = No2;
    }
    return Ans;
}

int main()                          
{
    cout<<Maximum(21.2f,11.2f)<<"\n";
    cout<<Maximum(21.2,11.2)<<"\n";
    cout<<Maximum(21,11)<<"\n";

    return 0;
}

/*
21.2
21.2
21
*/
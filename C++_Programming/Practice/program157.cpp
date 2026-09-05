#include<iostream>
using namespace std;

#pragma pack(1)
class ArrayX
{
    public:
        int *Arr;
        int iSize;

    ArrayX()                // Default constructor
    {

    }
    ArrayX(int X)           //parametrized constructor
    {

    }
};

int main()
{
    ArrayX aobj1;            // Default
    ArrayX aobj2(5);        // Parametrized      

    cout<<sizeof(aobj1)<<endl;      

    return 0;
}
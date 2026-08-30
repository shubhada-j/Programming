#include<iostream>
using namespace std;

#pragma pack(1)
class ArrayX
{
    public:
        int *Arr;
        int iSize;

    ArrayX(int X)           //parametrized constructor
    {

    }
};

int main()
{
    ArrayX aobj();            //ERROR -> due to not passing parameter but using parametrized constructor

    cout<<sizeof(aobj)<<endl;      

    return 0;
}